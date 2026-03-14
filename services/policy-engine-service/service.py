import sys
import os
import redis
from datetime import datetime
import time

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.policy_approved_signal_event import PolicyApprovedSignalEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "validated_signals"
OUTPUT_STREAM = "policy_approved_signals"

last_id = "$"

# Example rules
ALLOWED_SYMBOLS = ["XAUUSD"]
MAX_TRADES_PER_SYMBOL = 10

symbol_trade_count = {}


def check_trading_hours():

    hour = datetime.utcnow().hour

    # Example trading window
    if 0 <= hour <= 23:
        return True

    return False


def check_symbol(symbol):

    return symbol in ALLOWED_SYMBOLS


def check_trade_limit(symbol):

    count = symbol_trade_count.get(symbol, 0)

    if count >= MAX_TRADES_PER_SYMBOL:
        return False

    return True


def publish_policy_signal(data):

    symbol = data["symbol"]

    event = PolicyApprovedSignalEvent(
        symbol=symbol,
        signal=data["signal"],
        confidence=float(data["confidence"]),
        timestamp=datetime.utcnow()
    )

    payload = event.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    symbol_trade_count[symbol] = symbol_trade_count.get(symbol, 0) + 1

    print("policy approved:", payload)


def main():

    global last_id

    print("Policy Engine Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                symbol = data["symbol"]

                if not check_trading_hours():
                    print("rejected (session):", data)

                elif not check_symbol(symbol):
                    print("rejected (symbol):", data)

                elif not check_trade_limit(symbol):
                    print("rejected (limit):", data)

                else:
                    publish_policy_signal(data)

                last_id = msg_id


if __name__ == "__main__":
    main()
