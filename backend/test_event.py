from app.domain.entities.enterprise_event import (
    EnterpriseEvent,
    EventSeverity,
)

event = EnterpriseEvent(
    event_type="CPU_HIGH",
    source="Server-01",
    description="CPU usage exceeded 90%",
    severity=EventSeverity.HIGH,
)

print(event)