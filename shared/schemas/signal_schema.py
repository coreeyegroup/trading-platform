from pydantic import BaseModel
from datetime import datetime


class StrategySignal(BaseModel):

    strategy: str
    symbol: str
    signal: str
    confidence: float
    created_at: datetime


class ValidatedSignal(BaseModel):

    strategy: str
    symbol: str
    signal: str
    confidence: float
    created_at: datetime
