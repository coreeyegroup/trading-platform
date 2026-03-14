"""
Signal repository.

Handles persistence of trading signals.
"""

from shared.database.session import get_session
from shared.database.models.signals import Signal


class SignalRepository:

    def insert_signal(self, signal_data: dict):
        """
        Insert a new signal into the database.
        """

        session = get_session()

        try:

            signal = Signal(**signal_data)

            session.add(signal)

            session.commit()

        except Exception as e:

            session.rollback()
            raise e

        finally:

            session.close()
