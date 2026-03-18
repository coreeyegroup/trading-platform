import json
import redis
from shared.retry_handler import handle_retry_or_dlq

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def create_consumer_group(stream, group):
    try:
        r.xgroup_create(stream, group, id="0", mkstream=True)
    except redis.exceptions.ResponseError:
        pass


def consume_events(stream, group, consumer, handler):
    while True:
        messages = r.xreadgroup(
            groupname=group,
            consumername=consumer,
            streams={stream: ">"},
            count=10,
            block=5000
        )

        if not messages:
            continue

        for stream_name, msgs in messages:
            for msg_id, msg_data in msgs:
                event = json.loads(msg_data["data"])

                try:
                    handler(event)
                    r.xack(stream, group, msg_id)

                except Exception as e:
                    print(f"ERROR: {e}")
                    handle_retry_or_dlq(stream, group, msg_id, msg_data)
