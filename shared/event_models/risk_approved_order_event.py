from pydantic import BaseModel
from datetime import datetime


class RiskApprovedOrderEvent(BaseModel):

    symbol: str
    side: str
    lot_size: float
    risk_percent: float
    timestamp: datetime
