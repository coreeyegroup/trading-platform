from db import conn


def save_metrics(symbol, position_size, avg_price, market_price, pnl):

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO account_metrics(
            symbol,
            position_size,
            avg_price,
            market_price,
            unrealized_pnl
        )
        VALUES(%s,%s,%s,%s,%s)
        """,
        (symbol, position_size, avg_price, market_price, pnl)
    )

    conn.commit()
