from shared.events.event_publisher import EventPublisher


class PolicyEngineHandler:

    def __init__(self):

        self.publisher = EventPublisher()

        # simple policy configuration
        self.allowed_symbols = ["XAUUSD", "EURUSD"]
        self.enabled_strategies = ["trend_strategy"]

    def handle(self, event):

        signal = event["data"]

        print("Policy engine received:", signal)

        # Policy: symbol whitelist
        if signal["symbol"] not in self.allowed_symbols:
            print("Policy rejected: symbol not allowed")
            return

        # Policy: strategy enable/disable
        if signal["strategy"] not in self.enabled_strategies:
            print("Policy rejected: strategy disabled")
            return

        # If passed all checks → approve signal
        print("Policy approved signal")

        self.publisher.publish(
            "policy_approved_signals",
            signal,
	    "policy_approved_signal"
        )

