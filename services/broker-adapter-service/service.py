import sys
import os
import redis
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from shared.config import REDIS_HOST, REDIS_PORT
from shared.event_models.execution_report_event import ExecutionReportEvent


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

INPUT_STREAM = "execution_orders"
OUTPUT_STREAM = "execution_reports"

last_id = "$"


def execute_order(data):

    # simulate broker execution
    status = "FILLED"

    report = ExecutionReportEvent(
        symbol=data["symbol"],
        side=data["side"],
        lot_size=float(data["lot_size"]),
        status=status,
        timestamp=datetime.utcnow()
    )

    payload = report.model_dump()
    payload["timestamp"] = payload["timestamp"].isoformat()

    redis_client.xadd(OUTPUT_STREAM, payload)

    print("execution report:", payload)


def main():

    global last_id

    print("Broker Adapter Started")

    while True:

        events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

        for stream, messages in events:

            for msg_id, data in messages:

                execute_order(data)

                last_id = msg_id


if __name__ == "__main__":
    main()
