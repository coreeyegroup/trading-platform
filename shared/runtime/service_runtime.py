import redis
import json
import time
import uuid
from shared.config import REDIS_HOST, REDIS_PORT


class ServiceRuntime:

    def __init__(self, stream_name, handler):

        self.stream = stream_name
        self.handler = handler

        self.group = stream_name + "_group"
        self.consumer = str(uuid.uuid4())

        self.redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

        self._ensure_consumer_group()

    def _ensure_consumer_group(self):
        try:
            self.redis.xgroup_create(
                self.stream,
                self.group,
                id="$",
                mkstream=True
            )
        except redis.exceptions.ResponseError:
            pass

    def start(self):

        print(f"Starting service runtime for stream: {self.stream}")

        while True:

            try:

                messages = self.redis.xreadgroup(
                    groupname=self.group,
                    consumername=self.consumer,
                    streams={self.stream: ">"},
                    count=10,
                    block=5000
                )

                if not messages:
                    continue

                for stream, entries in messages:

                    for msg_id, data in entries:

                        try:

                            raw_event = data["event"]
                            event = json.loads(raw_event)

                            self.handler.handle(event)

                            self.redis.xack(
                                self.stream,
                                self.group,
                                msg_id
                            )

                        except Exception as e:

                            print("Event processing error:", e)

            except Exception as e:

                print("Runtime error:", e)
                time.sleep(1)
