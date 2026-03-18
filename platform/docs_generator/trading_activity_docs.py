import psycopg2
from datetime import datetime

OUTPUT_FILE = "docs/auto/trading_activity.md"


def get_recent_rows(query):

    try:
        conn = psycopg2.connect(
            dbname="trading_system",
            user="trading",
            password="trading",
            host="localhost",
            port=5432
        )

        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        conn.close()

        return rows

    except Exception:
        return []


def generate_activity():

    signals = get_recent_rows(
        "SELECT * FROM signals ORDER BY id DESC LIMIT 10"
    )

    orders = get_recent_rows(
        "SELECT * FROM orders ORDER BY id DESC LIMIT 10"
    )

    trades = get_recent_rows(
        "SELECT * FROM trades ORDER BY id DESC LIMIT 10"
    )

    lines = []

    lines.append("# Trading Activity\n")
    lines.append(f"Last updated: {datetime.utcnow()} UTC\n")

    lines.append("## Recent Signals\n")

    for s in signals:
        lines.append(f"- {s}")

    lines.append("\n## Recent Orders\n")

    for o in orders:
        lines.append(f"- {o}")

    lines.append("\n## Recent Trades\n")

    for t in trades:
        lines.append(f"- {t}")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_activity()
