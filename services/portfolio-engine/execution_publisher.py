import redis
import json

redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)


def publish_portfolio_update(data):

    redis_client.xadd(
        "portfolio_updates",
        {
            "data": json.dumps(data)
        }
    )
