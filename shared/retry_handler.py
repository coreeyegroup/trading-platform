import json
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

MAX_RETRIES = 3

def handle_retry_or_dlq(stream, group, msg_id, msg_data):
    retry_count = int(msg_data.get("retry_count", 0))

    if retry_count < MAX_RETRIES:
        msg_data["retry_count"] = retry_count + 1

        r.xadd(stream, msg_data)
    else:
        dlq_stream = f"dlq.{stream}"
        r.xadd(dlq_stream, msg_data)

    r.xack(stream, group, msg_id)