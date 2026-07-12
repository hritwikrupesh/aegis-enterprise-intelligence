from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class EnterpriseState:
    """
    Represents the current operational state of an enterprise.
    """

    infrastructure_health: float = 100.0
    operations_health: float = 100.0
    finance_health: float = 100.0
    customer_health: float = 100.0
    security_health: float = 100.0

    last_updated: datetime = field(default_factory=datetime.utcnow)