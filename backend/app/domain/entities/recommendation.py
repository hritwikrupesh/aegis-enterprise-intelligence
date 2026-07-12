from dataclasses import dataclass


@dataclass
class Recommendation:
    """
    Final recommendation produced by the AI.
    """

    strategy_name: str
    confidence: float
    explanation: str