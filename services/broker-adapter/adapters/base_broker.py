class BrokerInterface:

    def connect(self):
        raise NotImplementedError

    def submit_order(self, order):
        raise NotImplementedError

    def cancel_order(self, order_id):
        raise NotImplementedError

    def get_order_status(self, order_id):
        raise NotImplementedError

    def stream_executions(self):
        raise NotImplementedError
