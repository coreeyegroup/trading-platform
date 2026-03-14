from pydantic import BaseModel
from datetime import datetime


class PortfolioUpdateEvent(BaseModel):

    symbol: str
    position_size: float
    timestamp: datetime
