import sys
import os
import redis
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.validated_signal_event import ValidatedSignalEvent

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "trade_signals"
OUTPUT_STREAM = "validated_signals"

CONFIDENCE_THRESHOLD = 0.65

last_id = "$"


def validate_signal(data):

    try:

        confidence = float(data["confidence"])

        if confidence < CONFIDENCE_THRESHOLD:
            return False

        if data["signal"] not in ["BUY", "SELL"]:
            return False

        return True

    except:
        return False


def publish_signal(data):

    event = ValidatedSignalEvent(
        symbol=data["symbol"],
        signal=data["signal"],
        confidence=float(data["confidence"]),
        timestamp=datetime.utcnow()
    )

    payload = event.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    print("validated:", payload)


def main():

    global last_id

    print("Signal Validator Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                if validate_signal(data):
                    publish_signal(data)
                else:
                    print("rejected:", data)

                last_id = msg_id


if __name__ == "__main__":
    main()
