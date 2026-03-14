from shared.events.event_publisher import EventPublisher
from shared.schemas.signal_schema import StrategySignal
from pydantic import ValidationError


class SignalValidatorHandler:

    def __init__(self):
        self.publisher = EventPublisher()

    def handle(self, event):

        try:
            signal = StrategySignal(**event["data"])

        except ValidationError as e:
            print("Schema validation failed:", e)
            return

        print("Signal validated:", signal)

        self.publisher.publish(
            "validated_signals",
            signal.model_dump(mode="json"),
            "validated_signal"
        )

