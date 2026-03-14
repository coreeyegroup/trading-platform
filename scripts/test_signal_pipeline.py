import sys
import os
from datetime import datetime

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.database.repositories.signal_repository import SignalRepository
from shared.events.event_publisher import EventPublisher


def run_test():

    repo = SignalRepository()
    publisher = EventPublisher()

    signal = {
        "strategy": "trend_following",
        "symbol": "XAUUSD",
        "signal": "BUY",
        "confidence": 0.85,
        "created_at": datetime.utcnow()
    }

    # Persist to database
    repo.insert_signal(signal)

    # Publish event
    publisher.publish("strategy_signals", signal)

    print("Signal stored in DB and published to Redis")


if __name__ == "__main__":
    run_test()
