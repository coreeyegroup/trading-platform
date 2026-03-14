import sys
import os
import redis
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.execution_order_event import ExecutionOrderEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "risk_approved_orders"
OUTPUT_STREAM = "execution_orders"

ORDER_TYPE = "MARKET"

last_id = "$"


def publish_execution_order(data):

    order = ExecutionOrderEvent(
        symbol=data["symbol"],
        side=data["side"],
        lot_size=float(data["lot_size"]),
        order_type=ORDER_TYPE,
        timestamp=datetime.utcnow()
    )

    payload = order.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    print("execution order:", payload)


def main():

    global last_id

    print("Execution Engine Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                publish_execution_order(data)

                last_id = msg_id


if __name__ == "__main__":
    main()
