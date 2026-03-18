import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def publish_metrics(data):

    redis_client.xadd(
        "account_metrics",
        {
            "data": json.dumps(data)
        }
    )
