from pathlib import Path

from app.simulation.clock import SimulationClock
from app.simulation.environment import SimulationEnvironment
from app.simulation.scenario_loader import ScenarioLoader


class SimulationEngine:
    """
    Coordinates the complete simulation.
    """

    def __init__(self):
        self.clock = SimulationClock()
        self.environment = SimulationEnvironment()
        self.loader = ScenarioLoader(
            Path("app/configs/scenarios")
        )

    def run(self):
        scenario = self.loader.load("marketing_campaign.json")

        print("Scenario Loaded")
        print(scenario)
        print()

        print(self.environment)
        print()

        self.clock.tick(5)

        print(self.clock.current_time)