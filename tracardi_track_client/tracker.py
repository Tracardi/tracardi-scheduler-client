import json

from tracardi_track_client.model.entity import Entity
from tracardi_track_client.model.event_payload import EventPayload
from tracardi_track_client.model.tracker_payload import TrackerPayload
import requests


def track(callback_url, source_id, profile_id, session_id, event_type, properties, context=None):
    if context is None:
        context = {}

    payload = TrackerPayload(
        source=Entity(id=source_id),
        session=Entity(id=session_id),
        profile=Entity(id=profile_id)
    )
    event = EventPayload(type=event_type, properties=properties)
    payload.add_event(event)

    payload.context = context
    data = json.dumps(payload.dict(), default=str)
    response = requests.post(f"{callback_url}/track", data=data)

    print(response.status_code, response.json())


if __name__ == "__main__":
    track(
        callback_url="http://localhost:8686",
        source_id="269c443c-640b-495f-8a24-3bcde8bae172",
        profile_id='1',
        session_id="1",
        event_type="test",
        properties={}
    )
