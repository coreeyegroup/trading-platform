import sys
import os
import redis
from datetime import datetime
import random

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.signal_event import SignalEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "market_context"
OUTPUT_STREAM = "trade_signals"

last_id = "$"


def generate_signal(data):

    trend = data["trend"]
    momentum = data["momentum"]
    volatility = float(data["volatility"])

    if trend == "up" and momentum == "positive":

        signal = "BUY"

    elif trend == "down" and momentum == "negative":

        signal = "SELL"

    else:

        signal = "HOLD"

    confidence = round(random.uniform(0.6, 0.9), 2)

    return signal, confidence


def publish_signal(symbol, signal, confidence):

    signal_event = SignalEvent(
        symbol=symbol,
        signal=signal,
        confidence=confidence,
        timestamp=datetime.utcnow()
    )

    event = signal_event.model_dump()

    event["timestamp"] = event["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, event)

    print("signal:", event)


def main():

    global last_id

    print("Strategy Engine Started")

    while True:

        events = redis_client.xreadgroup(
	    groupname="strategy-engine-group",
	    consumername="worker-1",
	    streams={INPUT_STREAM: ">"},
	    count=10,
	    block=5000
	)

        for stream, messages in events:

            for msg_id, data in messages:

                symbol = data["symbol"]

                signal, confidence = generate_signal(data)

                if signal != "HOLD":

                    publish_signal(symbol, signal, confidence)

                redis_client.xack(INPUT_STREAM, "strategy-engine-group", msg_id)


if __name__ == "__main__":
    main()
