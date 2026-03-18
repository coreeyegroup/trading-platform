import redis
import json

from broker_router import get_broker
from order_mapper import normalize_order
from execution_publisher import publish_execution
from execution_tracker import save_execution


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

STREAM = "execution_orders"
GROUP = "broker_group"
CONSUMER = "broker_worker_1"


def process_orders():

    print("Broker Adapter Started")

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

                    order = json.loads(data["order"])

                    order = normalize_order(order)

                    broker = get_broker(order["broker"])

                    report = broker.submit_order(order)

                    # Save execution
                    save_execution(report)

                    # Publish execution
                    publish_execution(report)

                    # ACK message
                    redis_client.xack(STREAM, GROUP, entry_id)

                except Exception as e:

                    print("Order processing error:", e)


if __name__ == "__main__":
    process_orders()