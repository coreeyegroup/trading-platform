import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.events.redis_client import redis_client


def test_redis():

    try:

        redis_client.ping()

        print("Redis connection SUCCESS")

    except Exception as e:

        print("Redis connection FAILED")
        print(e)


if __name__ == "__main__":
    test_redis()
