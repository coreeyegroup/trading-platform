"""
SQLAlchemy database engine.
Handles connection to PostgreSQL.
"""

from sqlalchemy import create_engine
from .config import DATABASE_URL

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)
