from pydantic import BaseModel
from datetime import datetime

class ContextEvent(BaseModel):

    symbol: str
    trend: str
    volatility: float
    momentum: str
    timestamp: datetime
