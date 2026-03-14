import sys
import os
import redis
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.risk_approved_order_event import RiskApprovedOrderEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "policy_approved_signals"
OUTPUT_STREAM = "risk_approved_orders"

ACCOUNT_BALANCE = 10000
RISK_PER_TRADE = 0.01

last_id = "$"


def calculate_position_size():

    risk_amount = ACCOUNT_BALANCE * RISK_PER_TRADE

    # simulated stop loss value
    stop_loss_value = 100

    lot_size = risk_amount / stop_loss_value

    return round(lot_size, 2)


def publish_order(data):

    lot_size = calculate_position_size()

    order = RiskApprovedOrderEvent(
        symbol=data["symbol"],
        side=data["signal"],
        lot_size=lot_size,
        risk_percent=RISK_PER_TRADE,
        timestamp=datetime.utcnow()
    )

    payload = order.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    print("risk approved order:", payload)


def main():

    global last_id

    print("Risk Engine Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                publish_order(data)

                last_id = msg_id


if __name__ == "__main__":
    main()
