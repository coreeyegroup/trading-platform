import redis
import time

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

INPUT_STREAM = "risk_approved_orders"
OUTPUT_STREAM = "execution_orders"

MAX_TRADES = 50

trade_count = 0
trading_enabled = True

last_id = "$"

print("Kill Switch Service Started")

while True:

    events = redis_client.xread({INPUT_STREAM: last_id}, block=0)

    for stream, messages in events:

        for msg_id, data in messages:

            if not trading_enabled:
                print("Trading halted by kill switch")
                last_id = msg_id
                continue

            trade_count += 1

            if trade_count > MAX_TRADES:
                trading_enabled = False
                print("KILL SWITCH ACTIVATED")
                continue

            redis_client.xadd(OUTPUT_STREAM, data)

            print("order allowed:", data)

            last_id = msg_id

    time.sleep(1)
