import uuid
from datetime import datetime, timezone

def create_event(event_type, source, payload, correlation_id=None):
    return {
        "event_id": str(uuid.uuid4()),
        "correlation_id": correlation_id or str(uuid.uuid4()),
        "event_type": event_type,
        "source": source,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "payload": payload
    }