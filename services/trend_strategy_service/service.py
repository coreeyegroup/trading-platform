import sys
import os

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.runtime.service_runtime import ServiceRuntime
from handler import TrendStrategyHandler


INPUT_STREAM = "strategy_inputs"


def main():

    runtime = ServiceRuntime(
        stream_name=INPUT_STREAM,
        handler=TrendStrategyHandler()
    )

    runtime.start()


if __name__ == "__main__":
    main()
