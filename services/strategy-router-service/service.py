import sys
import os
import redis
from datetime import datetime

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.strategy_input_event import StrategyInputEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "market_context"
OUTPUT_STREAM = "strategy_inputs"

last_id = "$"


def publish_strategy_input(data):

    event = StrategyInputEvent(
        symbol=data["symbol"],
        trend=data["trend"],
        volatility=float(data["volatility"]),
        momentum=data["momentum"],
        timestamp=datetime.utcnow()
    )

    event_data = event.model_dump()
    event_data["timestamp"] = event_data["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, event_data)

    print("strategy input:", event_data)


def main():

    global last_id

    print("Strategy Router Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                publish_strategy_input(data)

                last_id = msg_id


if __name__ == "__main__":
    main()
