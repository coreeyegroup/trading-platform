import json
from datetime import datetime
from .redis_client import redis_client


class EventPublisher:

    def _serialize(self, obj):
        """
        Convert non-JSON types into serializable format.
        """

        if isinstance(obj, datetime):
            return obj.isoformat()

        raise TypeError(f"Type {type(obj)} not serializable")


    def publish(self, stream_name: str, event: dict):

        redis_client.xadd(
            stream_name,
            {"data": json.dumps(event, default=self._serialize)}
        )
