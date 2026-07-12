from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import uuid4


@dataclass
class Enterprise:
    """
    Represents an enterprise within the Aegis platform.

    This is the root domain entity that contains the
    high-level information about an organization.
    """

    name: str
    industry: str
    country: str

    id: str = field(default_factory=lambda: str(uuid4()))
    departments: List[str] = field(default_factory=list)
    applications: List[str] = field(default_factory=list)
    business_goals: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)