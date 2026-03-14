import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def publish_event(stream, data):
    redis_client.xadd(stream, data)
