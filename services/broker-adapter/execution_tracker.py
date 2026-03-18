import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="trading_system",
    user="trading",
    password="tradingpass"
)


def save_execution(report):

    cursor = conn.cursor()

    query = """
    INSERT INTO executions (
        execution_id,
        order_id,
        symbol,
        side,
        quantity,
        price,
        status,
        broker
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            report["execution_id"],
            report["order_id"],
            report["symbol"],
            report["side"],
            report["quantity"],
            report["price"],
            report["status"],
            report["broker"]
        )
    )

    conn.commit()
