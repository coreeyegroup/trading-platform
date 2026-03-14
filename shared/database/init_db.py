"""
Initialize database tables.
"""

from .engine import engine
from .base import Base

# import models to register metadata
from .models import (
    accounts,
    orders,
    order_events,
    execution_reports,
    trades,
    positions,
    position_history,
    signals,
    strategy_registry,
    strategy_parameters,
    portfolio,
    risk_events,
    performance_metrics,
    system_logs,
)


def init_db():
    """
    Create all tables if they do not exist.
    """

    Base.metadata.create_all(bind=engine)
