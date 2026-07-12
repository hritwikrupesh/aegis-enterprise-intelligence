import json
from pathlib import Path

from app.domain.entities.scenario import Scenario


class ScenarioLoader:
    """
    Loads simulation scenarios from JSON configuration files.
    """

    def __init__(self, config_directory: Path):
        self.config_directory = config_directory

    def load(self, filename: str) -> Scenario:
        file_path = self.config_directory / filename

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Scenario(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            category=data["category"],
            duration_minutes=data["duration_minutes"],
            probability=data["probability"],
            effects=data["effects"],
        )