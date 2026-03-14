import json
from redis import Redis
from shared.events.event_envelope import create_event


class EventPublisher:

    def __init__(self):

        self.redis = Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def publish(self, stream, data, event_type):

        event = create_event(event_type, data)

        self.redis.xadd(
            stream,
            {"event": json.dumps(event)}
        )
