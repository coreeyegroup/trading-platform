import json
import time
import redis


class ServiceRuntime:
    def __init__(self, stream_name, handler):
        self.stream_name = stream_name
        self.handler = handler

        self.redis_client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

        # last processed message id
        self.last_id = "0"

    def start(self):
        print(f"Starting service runtime for stream: {self.stream_name}")

        while True:
            try:
                messages = self.redis_client.xread(
                    {self.stream_name: self.last_id},
                    block=5000,
                    count=10
                )

                if not messages:
                    continue

                for stream, stream_messages in messages:
                    for message_id, message_data in stream_messages:

                        self.last_id = message_id

                        try:
                            raw_event = message_data.get("event")

                            if raw_event is None:
                                print("Skipping malformed event:", message_data)
                                continue

                            event = json.loads(raw_event)

                            # pass full event envelope to handler
                            self.handler.handle(event)

                        except Exception as e:
                            print("Event processing error:", e)

            except Exception as e:
                print("Runtime error:", e)
                time.sleep(1)

