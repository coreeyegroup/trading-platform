from datetime import datetime

from shared.runtime.event_handler import EventHandler
from shared.database.repositories.signal_repository import SignalRepository
from shared.events.event_publisher import EventPublisher


STRATEGY_NAME = "trend_strategy"


class TrendStrategyHandler(EventHandler):

    def __init__(self):
        self.repo = SignalRepository()
        self.publisher = EventPublisher()

    def generate_signal(self, trend, momentum):

        if trend == "up" and momentum == "positive":
            return "BUY", 0.75

        if trend == "down" and momentum == "negative":
            return "SELL", 0.75

        return None, None

    def handle(self, event):

        symbol = event["symbol"]
        trend = event["trend"]
        momentum = event["momentum"]

        signal, confidence = self.generate_signal(trend, momentum)

        if not signal:
            return

        signal_data = {
            "strategy": STRATEGY_NAME,
            "symbol": symbol,
            "signal": signal,
            "confidence": confidence,
            "created_at": datetime.utcnow()
        }

        # Save to database
        self.repo.insert_signal(signal_data)

        # Publish to next stage
        self.publisher.publish("strategy_signals", signal_data)

        print("strategy signal:", signal_data)
