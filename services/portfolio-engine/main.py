import redis
import json

from portfolio_processor import process_execution
from execution_publisher import publish_portfolio_update


# ✅ FIRST: create client
redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)

# ✅ THEN: test connection
print("Connecting to Redis...")
print(redis_client.ping())


STREAM = "execution_reports"
GROUP = "portfolio_group"
CONSUMER = "portfolio_worker_1"


def process_orders():

    print("Portfolio Engine Started")

    while True:

        messages = redis_client.xreadgroup(
            groupname=GROUP,
            consumername=CONSUMER,
            streams={STREAM: ">"},
            count=10,
            block=5000
        )

        if not messages:
            continue

        for stream, entries in messages:

            for entry_id, data in entries:

                try:

                    report = json.loads(data["report"])

                    print("Processing:", report["execution_id"])

                    update = process_execution(report)

                    if update:
                        publish_portfolio_update(update)

                    redis_client.xack(STREAM, GROUP, entry_id)

                except Exception as e:

                    print("Portfolio error:", e)

                    from db import conn
                    conn.rollback()

                    redis_client.xack(STREAM, GROUP, entry_id)


if __name__ == "__main__":
    process_orders()