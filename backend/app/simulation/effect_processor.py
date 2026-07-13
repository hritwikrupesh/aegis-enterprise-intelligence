from app.domain.entities.scenario import Scenario
from app.simulation.environment import SimulationEnvironment


class EffectProcessor:
    """
    Applies scenario effects and records the changes.
    """

    def apply(
        self,
        scenario: Scenario,
        environment: SimulationEnvironment,
    ) -> dict:

        changes = {}

        for metric, value in scenario.effects.items():

            previous_value = getattr(environment, metric)

            current_value = previous_value + value

            setattr(environment, metric, current_value)

            changes[metric] = {
                "previous": previous_value,
                "current": current_value,
            }

        return changes