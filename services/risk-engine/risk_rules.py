from exposure_limits import ExposureLimits
from portfolio_limits import PortfolioLimits


class RiskRules:

    def __init__(self):
        self.exposure = ExposureLimits()
        self.portfolio = PortfolioLimits()

    def evaluate(self, signal, portfolio_state):

        if not self.portfolio.check_daily_loss(
            portfolio_state["daily_pnl"],
            portfolio_state["balance"]
        ):
            return False

        if not self.exposure.check_symbol_positions(
            portfolio_state["symbol_positions"]
        ):
            return False

        return True
