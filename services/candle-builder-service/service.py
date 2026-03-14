import sys
import os
import time
import redis
from datetime import datetime

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.candle_event import CandleEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

TICK_STREAM = "market_ticks"
CANDLE_STREAM = "market_candles"

last_id = "$"

candles = {}


def process_tick(data):

    symbol = data["symbol"]
    price = float(data["price"])
    volume = int(data["volume"])

    if symbol not in candles:

        candles[symbol] = {
            "open": price,
            "high": price,
            "low": price,
            "close": price,
            "volume": volume
        }

    else:

        candle = candles[symbol]

        candle["high"] = max(candle["high"], price)
        candle["low"] = min(candle["low"], price)
        candle["close"] = price
        candle["volume"] += volume


def publish_candles():

    for symbol, candle in candles.items():

        candle_event = CandleEvent(
            symbol=symbol,
            open=candle["open"],
            high=candle["high"],
            low=candle["low"],
            close=candle["close"],
            volume=candle["volume"],
            timestamp=datetime.utcnow()
        )

        event = candle_event.model_dump()

        # Convert datetime to string for Redis
        event["timestamp"] = event["timestamp"].isoformat()

        redis_client.xadd(CANDLE_STREAM, event)

        print("candle:", event)


def main():

    global last_id

    print("Candle Builder Service Started")

    while True:

        events = redis_client.xread({TICK_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                process_tick(data)

                last_id = msg_id

        time.sleep(5)

        if candles:
            publish_candles()
            candles.clear()


if __name__ == "__main__":
    main()
