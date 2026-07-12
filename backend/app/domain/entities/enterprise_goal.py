from dataclasses import dataclass


@dataclass
class EnterpriseGoal:
    """
    Represents a business objective.
    """

    name: str
    description: str
    priority: int
    target_value: float
    current_value: float