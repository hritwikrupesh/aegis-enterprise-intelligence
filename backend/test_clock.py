from datetime import datetime

from app.simulation.clock import EnterpriseClock

clock = EnterpriseClock(
    current_time=datetime(2026, 7, 15, 9, 0)
)

print(clock.current_time)
print(clock.is_business_hours())

clock.tick(30)

print(clock.current_time)