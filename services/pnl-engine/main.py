import redis
import json

from pnl_processor import process_portfolio_update
from pnl_publisher import publish_metrics


# -------------------------------
# Redis Connection
# -------------------------------
redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)

print("Connecting to Redis...")
print(redis_client.ping())


# -------------------------------
# Stream Config
# -------------------------------
STREAM = "portfolio_updates"
GROUP = "pnl_group"
CONSUMER = "pnl_worker_1"


# -------------------------------
# Main Processing Loop
# -------------------------------
def process():

    print("PnL Engine Started")

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

                    # Parse incoming portfolio update
                    update = json.loads(data["data"])

                    print("PnL Processing:", update["symbol"])

                    # Compute metrics
                    metrics = process_portfolio_update(update)

                    # Publish downstream
                    publish_metrics(metrics)

                    # ACK message
                    redis_client.xack(STREAM, GROUP, entry_id)

                except Exception as e:

                    print("PnL error:", e)


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    process()