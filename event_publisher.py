import json
from .redis_client import redis_client


class EventPublisher:

    def publish(self, stream, event):

        redis_client.xadd(
            stream,
            {"data": json.dumps(event)}
        )
