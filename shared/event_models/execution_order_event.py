from pydantic import BaseModel
from datetime import datetime


class ExecutionOrderEvent(BaseModel):

    symbol: str
    side: str
    lot_size: float
    order_type: str
    timestamp: datetime
