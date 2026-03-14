from pydantic import BaseModel
from datetime import datetime


class StrategySignalEvent(BaseModel):

    strategy: str
    symbol: str
    signal: str
    confidence: float
    timestamp: datetime
