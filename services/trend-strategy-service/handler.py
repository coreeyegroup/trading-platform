from datetime import datetime
import random

from shared.events.event_publisher import EventPublisher


class TrendStrategyHandler:

    def __init__(self):

        self.publisher = EventPublisher()

    def handle(self, event):

        data = event["data"]

        symbol = data.get("symbol", "XAUUSD")

        side = random.choice(["BUY", "SELL"])

        confidence = round(random.uniform(0.6, 0.9), 2)

        signal = {
            "strategy": "trend_strategy",
            "symbol": symbol,
            "signal": side,
            "confidence": confidence,
            "created_at": datetime.utcnow().isoformat()
        }

        print("strategy signal:", signal)

        self.publisher.publish(
            "strategy_signals",
            signal,
            "strategy_signal"
        )
