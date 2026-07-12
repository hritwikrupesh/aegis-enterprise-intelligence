from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class EventSeverity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class EnterpriseEvent:
    """
    Represents a business or infrastructure event occurring
    within an enterprise.
    """

    event_type: str
    source: str
    description: str
    severity: EventSeverity

    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)