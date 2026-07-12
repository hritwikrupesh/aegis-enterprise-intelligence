from dataclasses import dataclass
from typing import Dict


@dataclass
class Scenario:
    """
    Represents a simulation scenario loaded from configuration.
    """

    id: str
    name: str
    description: str
    category: str
    duration_minutes: int
    probability: float
    effects: Dict[str, float]