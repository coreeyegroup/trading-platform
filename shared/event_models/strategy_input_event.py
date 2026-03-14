from pydantic import BaseModel
from datetime import datetime


class StrategyInputEvent(BaseModel):

    symbol: str
    trend: str
    volatility: float
    momentum: str
    timestamp: datetime
