from pathlib import Path

from app.simulation.scenario_loader import ScenarioLoader

loader = ScenarioLoader(
    Path("app/configs/scenarios")
)

scenario = loader.load("marketing_campaign.json")

print(scenario)