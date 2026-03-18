import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def publish_portfolio_update(update):

    redis_client.xadd(
        "portfolio_updates",
        {
            "data": json.dumps(update)
        }
    )
