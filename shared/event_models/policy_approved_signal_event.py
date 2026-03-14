from pydantic import BaseModel
from datetime import datetime


class PolicyApprovedSignalEvent(BaseModel):

    symbol: str
    signal: str
    confidence: float
    timestamp: datetime
