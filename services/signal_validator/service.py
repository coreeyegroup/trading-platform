from shared.runtime.service_runtime import ServiceRuntime
from handler import SignalValidatorHandler


def main():

    runtime = ServiceRuntime(
        stream_name="strategy_signals",
        handler=SignalValidatorHandler()
    )

    runtime.start()


if __name__ == "__main__":
    main()

