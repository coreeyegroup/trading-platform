from pydantic import BaseModel
from datetime import datetime


class TradeSignalEvent(BaseModel):

    symbol: str
    signal: str
    confidence: float
    strategies: int
    timestamp: datetime
