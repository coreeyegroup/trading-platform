import sys
import os
import redis
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.portfolio_update_event import PortfolioUpdateEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "execution_reports"
OUTPUT_STREAM = "portfolio_updates"

last_id = "$"

positions = {}


def update_position(data):

    symbol = data["symbol"]
    side = data["side"]
    lot_size = float(data["lot_size"])

    current = positions.get(symbol, 0)

    if side == "BUY":
        current += lot_size
    else:
        current -= lot_size

    positions[symbol] = current

    return current


def publish_portfolio_update(symbol, position_size):

    update = PortfolioUpdateEvent(
        symbol=symbol,
        position_size=position_size,
        timestamp=datetime.utcnow()
    )

    payload = update.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    print("portfolio update:", payload)


def main():

    global last_id

    print("Portfolio Engine Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                symbol = data["symbol"]

                position_size = update_position(data)

                publish_portfolio_update(symbol, position_size)

                last_id = msg_id


if __name__ == "__main__":
    main()
