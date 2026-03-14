"""
Signal model.

Represents strategy-generated trading signals.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from shared.database.base import Base


class Signal(Base):

    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)

    strategy = Column(String(50))

    symbol = Column(String(20))

    signal = Column(String(10))   # BUY / SELL

    confidence = Column(Float)

    created_at = Column(DateTime)
