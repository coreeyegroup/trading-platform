from fastapi import FastAPI
from redis_client import publish_event

app = FastAPI(
    title="Trading Platform API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"status": "Trading Platform Running"}

@app.post("/tick")
async def publish_tick():

    data = {
        "symbol": "XAUUSD",
        "price": "2200"
    }

    publish_event("market_ticks", data)

    return {"event": "tick published"}
