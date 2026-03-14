from pydantic import BaseModel
from datetime import datetime


class ValidatedSignalEvent(BaseModel):

    symbol: str
    signal: str
    confidence: float
    timestamp: datetime
