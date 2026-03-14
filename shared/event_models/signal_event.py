from pydantic import BaseModel
from datetime import datetime


class SignalEvent(BaseModel):

    symbol: str
    signal: str
    confidence: float
    timestamp: datetime
