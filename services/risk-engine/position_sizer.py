class PositionSizer:

    def __init__(self, account_balance: float, risk_per_trade: float = 0.01):
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, entry_price, stop_loss, contract_size=100000):

        risk_amount = self.account_balance * self.risk_per_trade
        stop_distance = abs(entry_price - stop_loss)

        if stop_distance == 0:
            return 0

        position_size = risk_amount / (stop_distance * contract_size)

        return round(position_size, 4)
