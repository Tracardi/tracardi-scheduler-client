from typing import Optional
from pydantic import BaseModel


class EventPayload(BaseModel):
    type: str
    properties: Optional[dict] = {}
    options: Optional[dict] = {}
    context: Optional[dict] = {}

