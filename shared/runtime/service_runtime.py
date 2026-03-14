"""
Universal service runtime.

Provides the execution loop for all trading microservices.
"""

import json
from shared.events.redis_client import redis_client


class ServiceRuntime:

    def __init__(self, stream_name, handler):
        """
        stream_name: Redis stream to consume
        handler: event processing handler
        """

        self.stream_name = stream_name
        self.handler = handler


    def start(self):

        print(f"Starting service runtime for stream: {self.stream_name}")

        last_id = "0-0"

        while True:

            messages = redis_client.xread(
                {self.stream_name: last_id},
                block=0
            )

            for stream, events in messages:

                for event_id, payload in events:

                    try:

                        data = payload.get("data")

                        if data:
                            event = json.loads(data)
                        else:
                            event = payload

                        self.handler.handle(event)

                        last_id = event_id

                    except Exception as e:

                        print("Event processing error:", e)
