import sys
import os
import redis
import time
from datetime import datetime

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.candle_event import CandleEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "market_candles"
OUTPUT_STREAM = "validated_candles"

last_id = "$"


def validate_candle(data):

    try:

        symbol = data["symbol"]

        open_price = float(data["open"])
        high = float(data["high"])
        low = float(data["low"])
        close = float(data["close"])
        volume = int(data["volume"])

        # Basic validation rules

        if open_price <= 0 or high <= 0 or low <= 0 or close <= 0:
            return False

        if high < low:
            return False

        if volume < 0:
            return False

        return True

    except Exception:
        return False


def publish_validated(data):

    candle = CandleEvent(
        symbol=data["symbol"],
        open=float(data["open"]),
        high=float(data["high"]),
        low=float(data["low"]),
        close=float(data["close"]),
        volume=int(data["volume"]),
        timestamp=datetime.utcnow()
    )

    event = candle.model_dump()

    event["timestamp"] = event["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, event)

    print("validated:", event)


def main():

    global last_id

    print("Data Integrity Service Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                if validate_candle(data):

                    publish_validated(data)

                else:

                    print("invalid candle detected:", data)

                last_id = msg_id


if __name__ == "__main__":
    main()
