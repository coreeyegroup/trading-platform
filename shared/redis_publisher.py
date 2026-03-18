import json
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def publish_event(stream_name, event):
    r.xadd(stream_name, {"data": json.dumps(event)})