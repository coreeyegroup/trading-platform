import json
from .redis_client import redis_client


class EventConsumer:
    """
    Basic Redis stream consumer.
    """

    def consume(self, stream_name: str, last_id="0-0"):

        messages = redis_client.xread(
            {stream_name: last_id},
            block=0
        )

        for stream, events in messages:
            for event_id, payload in events:
                data = json.loads(payload["data"])
                yield data
