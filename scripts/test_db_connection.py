import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from sqlalchemy import text
from shared.database.session import get_session


def test_connection():

    try:

        session = get_session()

        result = session.execute(text("SELECT 1"))

        print("Database connection SUCCESS")

        session.close()

    except Exception as e:

        print("Database connection FAILED")
        print(e)


if __name__ == "__main__":
    test_connection()
