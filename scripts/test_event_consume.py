import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.events.event_consumer import EventConsumer


def test_consume():

    consumer = EventConsumer()

    print("Listening for events...")

    for event in consumer.consume("test_stream"):
        print("Received event:")
        print(event)
        break


if __name__ == "__main__":
    test_consume()
