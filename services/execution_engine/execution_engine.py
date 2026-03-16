from shared.runtime.service_runtime import ServiceRuntime
from shared.events.event_publisher import EventPublisher


class ExecutionEngine:

    INPUT_STREAM = "risk_approved_orders"
    OUTPUT_STREAM = "execution_orders"

    def __init__(self):
        self.publisher = EventPublisher()

    def handle(self, event):

        import json

        order = event["data"]

        # ensure dictionary
        if isinstance(order, str):
            try:
                order = json.loads(order)
            except Exception:
                print("Skipping malformed order:", order)
                return

        if not isinstance(order, dict):
            print("Invalid order format:", order)
            return

        execution_order = {
            "symbol": order["symbol"],
            "side": order["side"],
            "size": order["size"],
            "order_type": "market",
            "strategy": order["strategy"],
            "signal_id": order.get("signal_id")
        }

        self.publisher.publish(
            self.OUTPUT_STREAM,
            execution_order,
            "execution_order"
        )

        print("Execution order created:", execution_order)


def main():

    engine = ExecutionEngine()

    runtime = ServiceRuntime(
        ExecutionEngine.INPUT_STREAM,
        engine
    )

    runtime.start()


if __name__ == "__main__":
    main()
