import redis
import json

# Create Redis connection
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def publish_execution(report):

    redis_client.xadd(
        "execution_reports",
        {
            "report": json.dumps(report)
        }
    )
