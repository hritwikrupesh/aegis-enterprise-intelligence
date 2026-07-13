from pathlib import Path

from app.simulation.clock import SimulationClock
from app.simulation.environment import SimulationEnvironment
from app.simulation.scenario_loader import ScenarioLoader
from app.simulation.event_generator import EventGenerator


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
        self.generator = EventGenerator()

    def run(self):
        scenario = self.loader.load("marketing_campaign.json")

        print("Scenario Loaded")
        print(scenario)
        print()

        events = self.generator.apply_scenario(
            scenario,
            self.environment,
        )
        print("Updated Environment")
        print(self.environment)

        print()
        print("Generated Events")

        for event in events:
            print(event)
        
        print()

        self.clock.tick(5)

        print(self.clock.current_time)