from pydantic import BaseModel
from datetime import datetime


class ExecutionReportEvent(BaseModel):

    symbol: str
    side: str
    lot_size: float
    status: str
    timestamp: datetime
