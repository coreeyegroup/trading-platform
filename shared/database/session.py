"""
Database session manager.
Provides SQLAlchemy sessions for services.
"""

from sqlalchemy.orm import sessionmaker
from .engine import engine

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_session():
    """
    Create and return a new database session.
    """

    return SessionLocal()
