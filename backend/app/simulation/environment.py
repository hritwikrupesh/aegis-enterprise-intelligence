from dataclasses import dataclass


@dataclass
class SimulationEnvironment:
    """
    Represents the current operational state
    of the simulated enterprise.
    """

    traffic: int = 1000
    cpu_usage: float = 25.0
    memory_usage: float = 30.0
    active_orders: int = 100
    warehouse_load: float = 20.0
    support_tickets: int = 5
    customer_satisfaction: float = 95.0
    cloud_cost: float = 100.0