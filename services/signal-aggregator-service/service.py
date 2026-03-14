import sys
import os
import redis
from datetime import datetime

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.trade_signal_event import TradeSignalEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "strategy_signals"
OUTPUT_STREAM = "trade_signals"

last_id = "$"

signal_buffer = {}


def process_signal(data):

    symbol = data["symbol"]
    signal = data["signal"]
    confidence = float(data["confidence"])

    if symbol not in signal_buffer:

        signal_buffer[symbol] = {
            "BUY": [],
            "SELL": []
        }

    signal_buffer[symbol][signal].append(confidence)


def aggregate_signals():

    for symbol, signals in signal_buffer.items():

        buy_count = len(signals["BUY"])
        sell_count = len(signals["SELL"])

        if buy_count == 0 and sell_count == 0:
            continue

        if buy_count > sell_count:

            final_signal = "BUY"
            confidence = sum(signals["BUY"]) / buy_count
            strategies = buy_count

        else:

            final_signal = "SELL"
            confidence = sum(signals["SELL"]) / sell_count
            strategies = sell_count

        publish_trade_signal(symbol, final_signal, confidence, strategies)


def publish_trade_signal(symbol, signal, confidence, strategies):

    event = TradeSignalEvent(
        symbol=symbol,
        signal=signal,
        confidence=confidence,
        strategies=strategies,
        timestamp=datetime.utcnow()
    )

    data = event.model_dump()
    data["timestamp"] = data["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, data)

    print("aggregated signal:", data)


def main():

    global last_id

    print("Signal Aggregator Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                process_signal(data)

                last_id = msg_id

        if signal_buffer:

            aggregate_signals()
            signal_buffer.clear()


if __name__ == "__main__":
    main()
