from pydantic import BaseModel


class Position(BaseModel):

    symbol: str
    quantity: float
    avg_price: float
