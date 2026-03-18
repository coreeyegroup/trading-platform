import subprocess
import redis
import psycopg2
from datetime import datetime

OUTPUT_FILE = "docs/auto/system_status.md"


def get_docker_services():

    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


def get_redis_streams():

    try:
        r = redis.Redis(host="localhost", port=6379)
        streams = r.keys("*")
        return [s.decode() for s in streams]

    except:
        return []


def get_db_tables():

    try:

        conn = psycopg2.connect(
            dbname="trading_system",
            user="trading",
            password="trading",
            host="localhost",
            port=5432
        )

        cur = conn.cursor()

        cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        """)

        tables = [t[0] for t in cur.fetchall()]

        return tables

    except:
        return []


def generate_status():

    services = get_docker_services()
    streams = get_redis_streams()
    tables = get_db_tables()

    lines = []

    lines.append("# Trading Platform System Status\n")

    lines.append(f"Last updated: {datetime.utcnow()} UTC\n")

    lines.append("## Running Services\n")

    for s in services:
        lines.append(f"- {s}")

    lines.append("\n## Redis Streams\n")

    for s in streams:
        lines.append(f"- {s}")

    lines.append("\n## Database Tables\n")

    for t in tables:
        lines.append(f"- {t}")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_status()
