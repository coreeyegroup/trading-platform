from shared.runtime.service_runtime import ServiceRuntime
from shared.events.event_publisher import publish_event

from position_sizer import PositionSizer
from risk_rules import RiskRules


class RiskEngine:

    INPUT_STREAM = "policy_approved_signals"
    OUTPUT_STREAM = "risk_approved_orders"

    def __init__(self):

        self.rules = RiskRules()

        self.sizer = PositionSizer(
            account_balance=10000,
            risk_per_trade=0.01
        )

    def handle_signal(self, event):

        signal = event["data"]

        portfolio_state = {
            "balance": 10000,
            "daily_pnl": 0,
            "symbol_positions": 1
        }

        approved = self.rules.evaluate(signal, portfolio_state)

        if not approved:
            print("Risk rejected signal")
            return

        size = self.sizer.calculate_position_size(
            signal["price"],
            signal["stop_loss"]
        )

        order = {
            "symbol": signal["symbol"],
            "side": signal["side"],
            "size": size,
            "strategy": signal["strategy"],
            "signal_id": signal.get("signal_id")
        }

        publish_event(self.OUTPUT_STREAM, order)

        print("Risk approved order:", order)


def main():

    engine = RiskEngine()

    runtime = ServiceRuntime(
        service_name="risk_engine",
        input_stream=RiskEngine.INPUT_STREAM,
        handler=engine.handle_signal
    )

    runtime.start()


if __name__ == "__main__":
    main()
