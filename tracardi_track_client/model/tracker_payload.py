from datetime import datetime
from typing import Optional, List, Any, Union
from uuid import uuid4

from pydantic import BaseModel

from .browser_context import BrowserContext
from .entity import Entity
from .event_payload import EventPayload
from .payload_options import PayloadOptions
from .time import Time


class EventPayloadMetadata(BaseModel):
    time: Time
    ip: str = None
    status: str = None


class TrackerPayload(BaseModel):
    source: Entity
    session: Entity = None

    metadata: Optional[EventPayloadMetadata]
    profile: Optional[Entity] = None
    context: Optional[Union[dict, BrowserContext]] = {}
    properties: Optional[dict] = {}
    events: List[EventPayload] = []
    options: Optional[PayloadOptions] = PayloadOptions()

    def __init__(self, **data: Any):
        data['metadata'] = EventPayloadMetadata(
            time=Time(
                insert=datetime.utcnow()
            )
        )

        super().__init__(**data)

        if self.session is None:
            self.session = Entity(id=str(uuid4()))

    def set_return_profile(self, profile=True):
        self.options.profile = profile

    def add_event(self, event: EventPayload):
        if not isinstance(event, EventPayload):
            raise ValueError("Param event is not EventPayload class.")
        self.events.append(event)

    def set_context(self, context: dict):
        self.context = context
        return self

    def set_profile(self, profile_id: str):
        self.profile = Entity(id=profile_id)
        return self

    def set_properties(self, props: dict):
        self.properties = props

    def serialize(self) -> dict:
        if len(self.events) == 0:
            raise ValueError("Events are empty")

        data = self.dict()
        data['metadata']['time'] = str(data['metadata']['time'])

        return data
