from datetime import datetime


def create_event(event_type: str, data: dict, version="1.0"):

    return {
        "event_type": event_type,
        "version": version,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
