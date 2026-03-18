import psycopg2

def is_processed(conn, event_id):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM processed_events WHERE event_id = %s",
            (event_id,)
        )
        return cur.fetchone() is not None


def mark_processed(conn, event_id, service_name):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO processed_events (event_id, service_name)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
            """,
            (event_id, service_name)
        )
    conn.commit()