import json
from datetime import datetime

from app.domain.entities.enterprise_event import EnterpriseEvent
from app.domain.enums.event_severity import EventSeverity


class CloudEventProcessor:
    """
    Converts Pub/Sub JSON messages into EnterpriseEvent objects.
    """

    def process(self, message: str) -> EnterpriseEvent:

        data = json.loads(message)

        return EnterpriseEvent(
            enterprise_id=data["enterprise_id"],
            scenario_id=data["scenario_id"],
            event_type=data["event_type"],
            metric=data["metric"],
            previous_value=data["previous_value"],
            current_value=data["current_value"],
            severity=EventSeverity(data["severity"]),
            source=data["source"],
            event_id=data["event_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )