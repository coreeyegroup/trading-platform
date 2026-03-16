from shared.runtime.service_runtime import ServiceRuntime
from handler import PolicyEngineHandler


def main():

    runtime = ServiceRuntime(
        stream_name="validated_signals",
        handler=PolicyEngineHandler()
    )

    runtime.start()


if __name__ == "__main__":
    main()

