from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class EnterpriseClock:
    """
    Simulates enterprise time.
    """

    current_time: datetime

    def tick(self, minutes: int = 1) -> None:
        """Advance simulated time."""
        self.current_time += timedelta(minutes=minutes)

    def is_business_hours(self) -> bool:
        """Return True if current time is between 9 AM and 6 PM."""
        return 9 <= self.current_time.hour < 18

    def is_weekend(self) -> bool:
        """Return True if Saturday or Sunday."""
        return self.current_time.weekday() >= 5

    def is_peak_hours(self) -> bool:
        """Return True during peak enterprise hours."""
        return 10 <= self.current_time.hour <= 14