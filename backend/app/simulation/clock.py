from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class SimulationClock:
    """
    Simulates time inside the enterprise simulation.
    """

    current_time: datetime = field(default_factory=datetime.now)

    def tick(self, minutes: int = 1) -> None:
        self.current_time += timedelta(minutes=minutes)

    def is_business_hours(self) -> bool:
        return 9 <= self.current_time.hour < 18

    def is_weekend(self) -> bool:
        return self.current_time.weekday() >= 5

    def is_peak_hours(self) -> bool:
        return 10 <= self.current_time.hour <= 14