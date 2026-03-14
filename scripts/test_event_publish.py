import sys
import os
import json

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.events.event_publisher import EventPublisher

def test_publish():

    publisher = EventPublisher()

    event = {
        "symbol": "XAUUSD",
        "price": 2000.50,
        "volume": 0.10,
        "type": "test_event"
    }

    publisher.publish("test_stream", event)

    print("Event published successfully")

if __name__ == "__main__":
    test_publish()
