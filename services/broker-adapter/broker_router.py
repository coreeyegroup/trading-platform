from adapters.mock_adapter import MockAdapter


BROKERS = {
    "mock": MockAdapter()
}


def get_broker(broker_name):

    broker = BROKERS.get(broker_name)

    if not broker:
        raise Exception(f"Broker not supported: {broker_name}")

    return broker
