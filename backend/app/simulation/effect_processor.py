from app.domain.entities.scenario import Scenario
from app.simulation.environment import SimulationEnvironment


class EffectProcessor:
    """
    Applies the direct effects of a scenario
    to the simulation environment.
    """

    def apply(
        self,
        scenario: Scenario,
        environment: SimulationEnvironment,
    ) -> None:

        for metric, value in scenario.effects.items():

            current_value = getattr(environment, metric)

            setattr(
                environment,
                metric,
                current_value + value,
            )