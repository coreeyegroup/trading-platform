from db import conn


def get_position(symbol):

    cursor = conn.cursor()

    cursor.execute(
        "SELECT symbol, position_size, avg_price FROM positions WHERE symbol=%s",
        (symbol,)
    )

    return cursor.fetchone()


def save_position(symbol, quantity, avg_price):

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO positions(symbol, position_size, avg_price)
        VALUES(%s,%s,%s)
        ON CONFLICT(symbol)
        DO UPDATE SET
        position_size = EXCLUDED.position_size,
        avg_price = EXCLUDED.avg_price,
        updated_at = NOW()
        """,
        (symbol, quantity, avg_price)
    )

    conn.commit()

def execution_exists(execution_id):

    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM executions WHERE execution_id=%s",
        (execution_id,)
    )

    return cursor.fetchone() is not None