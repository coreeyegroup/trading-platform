from pydantic import BaseModel
from datetime import datetime


class CandleEvent(BaseModel):

    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    timestamp: datetime
