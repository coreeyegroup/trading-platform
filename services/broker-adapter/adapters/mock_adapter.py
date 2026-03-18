import random
import time

from adapters.base_broker import BrokerInterface


class MockAdapter(BrokerInterface):

    def connect(self):
        return True

    def submit_order(self, order):

        time.sleep(1)

        price = round(random.uniform(1.10,1.20),5)

        return {
            "execution_id": "EXE_" + str(random.randint(1000,9999)),
            "order_id": order["order_id"],
            "symbol": order["symbol"],
            "side": order["side"],
            "quantity": order["quantity"],
            "price": price,
            "status": "FILLED",
            "broker": "mock"
        }
