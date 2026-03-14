import sys
import os
import time
import random
import redis
from datetime import datetime

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.tick_event import TickEvent

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

STREAM = "market_ticks"
SYMBOL = "XAUUSD"


def generate_tick():

    price = round(2200 + random.uniform(-1, 1), 2)

    tick = TickEvent(
        symbol=SYMBOL,
        price=price,
        volume=random.randint(1, 5),
        timestamp=datetime.utcnow(),
    )

    event = tick.model_dump()

    # Convert datetime for Redis
    event["timestamp"] = event["timestamp"].isoformat()

    return event


def publish_tick():

    event = generate_tick()

    redis_client.xadd(STREAM, event)

    print("tick:", event)


def main():

    print("Market Data Service Started")

    while True:

        publish_tick()

        time.sleep(1)


if __name__ == "__main__":
    main()
