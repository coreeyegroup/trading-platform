import sys
import os
import redis
import numpy as np
from datetime import datetime

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.context_event import ContextEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "validated_candles"
OUTPUT_STREAM = "market_context"

last_id = "$"

price_history = []


def compute_context(price):

    price_history.append(price)

    if len(price_history) > 20:
        price_history.pop(0)

    if len(price_history) < 5:
        return None

    trend = "up" if price_history[-1] > price_history[0] else "down"

    volatility = float(np.std(price_history))

    momentum = "positive" if price_history[-1] > price_history[-2] else "negative"

    return trend, volatility, momentum


def publish_context(symbol, trend, volatility, momentum):

    context = ContextEvent(
        symbol=symbol,
        trend=trend,
        volatility=volatility,
        momentum=momentum,
        timestamp=datetime.utcnow()
    )

    event = context.model_dump()

    event["timestamp"] = event["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, event)

    print("context:", event)


def main():

    global last_id

    print("Market Context Service Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                symbol = data["symbol"]
                close_price = float(data["close"])

                context = compute_context(close_price)

                if context:

                    trend, volatility, momentum = context

                    publish_context(symbol, trend, volatility, momentum)

                last_id = msg_id


if __name__ == "__main__":
    main()
