from pathlib import Path

from app.simulation.clock import SimulationClock
from app.simulation.environment import SimulationEnvironment
from app.simulation.scenario_loader import ScenarioLoader
from app.simulation.event_generator import EventGenerator
from app.simulation.effect_processor import EffectProcessor


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
        self.effect_processor = EffectProcessor()

    def run(self):
        scenario = self.loader.load("marketing_campaign.json")

        print("Scenario Loaded")
        print(scenario)
        print()

        self.effect_processor.apply(
            scenario,
            self.environment,
            )
        events = self.generator.generate(
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