class PortfolioLimits:

    MAX_DAILY_LOSS = 0.05

    def check_daily_loss(self, daily_pnl, account_balance):

        if abs(daily_pnl) > account_balance * self.MAX_DAILY_LOSS:
            return False

        return True
