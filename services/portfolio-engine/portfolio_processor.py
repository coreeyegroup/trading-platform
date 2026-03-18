from decimal import Decimal
from repository.position_repository import get_position, save_position, execution_exists


def process_execution(report):

    execution_id = report["execution_id"]

    # 🔒 IDEMPOTENCY CHECK
    if execution_exists(execution_id):
        print(f"Duplicate execution skipped: {execution_id}")
        return None

    symbol = report["symbol"]

    qty = Decimal(str(report["quantity"]))
    price = Decimal(str(report["price"]))
    side = report["side"]

    position = get_position(symbol)

    if position is None:

        new_qty = qty if side == "BUY" else -qty
        new_avg = price

    else:

        _, current_qty, avg_price = position

        current_qty = Decimal(current_qty)
        avg_price = Decimal(avg_price)

        new_qty = current_qty + qty if side == "BUY" else current_qty - qty

        if new_qty != 0:
            new_avg = ((current_qty * avg_price) + (qty * price)) / new_qty
        else:
            new_avg = Decimal("0")

    save_position(symbol, float(new_qty), float(new_avg))

    return {
        "symbol": symbol,
        "quantity": float(new_qty),
        "avg_price": float(new_avg)
    }