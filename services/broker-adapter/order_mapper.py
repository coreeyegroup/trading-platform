def normalize_order(order):

    return {
        "order_id": order["order_id"],
        "symbol": order["symbol"],
        "side": order["side"],
        "quantity": order["quantity"],
        "order_type": order.get("order_type","MARKET"),
        "broker": order.get("broker","mock")
    }
