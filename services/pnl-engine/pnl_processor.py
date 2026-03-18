from decimal import Decimal
from repository.pnl_repository import save_metrics


def process_portfolio_update(update):

    symbol = update["symbol"]

    qty = Decimal(str(update["quantity"]))
    avg_price = Decimal(str(update["avg_price"]))

    # MOCK market price (later from market data service)
    market_price = avg_price + Decimal("0.0020")

    pnl = (market_price - avg_price) * qty

    save_metrics(
        symbol,
        float(qty),
        float(avg_price),
        float(market_price),
        float(pnl)
    )

    return {
        "symbol": symbol,
        "position_size": float(qty),
        "avg_price": float(avg_price),
        "market_price": float(market_price),
        "unrealized_pnl": float(pnl)
    }
