from dataclasses import dataclass


@dataclass
class BusinessRule:
    """
    Represents a business rule evaluated during simulation.
    """

    metric: str
    operator: str
    threshold: float

    target: str
    adjustment: float

    description: str