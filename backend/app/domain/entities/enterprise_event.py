from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any
from uuid import uuid4
import json

from app.domain.enums.event_severity import EventSeverity


@dataclass
class EnterpriseEvent:
    """
    Standard enterprise event exchanged across the Aegis platform.
    """

    enterprise_id: str
    scenario_id: str

    event_type: str
    metric: str

    previous_value: Any
    current_value: Any

    severity: EventSeverity
    source: str

    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

    @property
    def change(self):
        if isinstance(self.previous_value, (int, float)) and isinstance(
            self.current_value, (int, float)
        ):
            return self.current_value - self.previous_value
        return None

    def to_dict(self):
        data = asdict(self)
        data["severity"] = self.severity.value
        data["timestamp"] = self.timestamp.isoformat()
        data["change"] = self.change
        return data

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)