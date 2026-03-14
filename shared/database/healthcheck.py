from .session import get_session


def check_database():

    try:

        session = get_session()

        session.execute("SELECT 1")

        session.close()

        return True

    except Exception as e:

        print("Database healthcheck failed:", e)

        return False
