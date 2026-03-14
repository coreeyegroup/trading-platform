from pydantic import BaseModel
from datetime import datetime


class TickEvent(BaseModel):

    symbol: str
    price: float
    volume: int
    timestamp: datetime
