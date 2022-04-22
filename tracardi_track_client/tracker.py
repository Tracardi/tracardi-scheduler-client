import json

from tracardi_track_client.model.entity import Entity
from tracardi_track_client.model.event_payload import EventPayload
from tracardi_track_client.model.tracker_payload import TrackerPayload
import requests


def track(callback_url, source_id, profile_id, session_id, event_type, properties, context=None):
    if context is None:
        context = {}

    if source_id is not None:

        payload = TrackerPayload(
            source=Entity(id=source_id),
            session=Entity(id=session_id) if session_id is not None else None,
            profile=Entity(id=profile_id) if profile_id is not None else None
        )

        event = EventPayload(type=event_type, properties=properties)
        event.context = context

        payload.add_event(event)

        data = json.dumps(payload.dict(), default=str)
        track_url = f"{callback_url}/track"
        response = requests.post(track_url, data=data)

        print(track_url, response.status_code, response.json())

    else:

        print("Missing source")


if __name__ == "__main__":
    track(
        callback_url="http://192.168.1.103:8686",
        source_id="d7a51074-d05d-4fbb-901e-bd494aa1bfb0",
        profile_id=None,
        session_id=None,
        event_type="test",
        properties={},
        context={"aaa": 1}
    )
