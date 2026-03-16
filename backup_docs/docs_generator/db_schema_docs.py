import psycopg2
import os

OUTPUT_FILE = "docs/auto/database_tables.md"

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "trading_system"),
    user=os.getenv("POSTGRES_USER", "trading"),
    password=os.getenv("POSTGRES_PASSWORD", "tradingpass"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=5432
)

def generate_docs():

    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
    """)

    tables = cur.fetchall()

    lines = []
    lines.append("# Database Tables\n")

    for t in tables:
        lines.append(f"- {t[0]}")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_docs()
