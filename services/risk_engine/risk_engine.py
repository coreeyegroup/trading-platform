from shared.runtime.service_runtime import ServiceRuntime
from shared.events.event_publisher import EventPublisher


class RiskEngine:

    INPUT_STREAM = "policy_approved_signals"
    OUTPUT_STREAM = "risk_approved_orders"

    def __init__(self):
        self.publisher = EventPublisher()

    def calculate_position_size(self, signal):
        return 0.01

    def handle(self, event):

        import json

        signal = event["data"]

        if isinstance(signal, str):
            signal = json.loads(signal)

        size = self.calculate_position_size(signal)

        order = {
            "symbol": signal["symbol"],
            "side": signal["signal"],
            "size": size,
            "strategy": signal["strategy"],
            "signal_id": signal.get("signal_id")
        }

        self.publisher.publish(
            self.OUTPUT_STREAM,
            "risk_approved_order",
    order
)

        print("Risk approved order:", order)


def main():

    engine = RiskEngine()

    runtime = ServiceRuntime(
        RiskEngine.INPUT_STREAM,
        engine
    )

    runtime.start()


if __name__ == "__main__":
    main()
