from app.domain.entities.enterprise_event import (
    EnterpriseEvent,
)
from app.domain.enums.event_severity import EventSeverity
from app.domain.entities.scenario import Scenario
from app.simulation.environment import SimulationEnvironment


class EventGenerator:
    """
    Applies scenario effects to the simulation environment
    and generates enterprise events.
    """

    def apply_scenario(
        self,
        scenario: Scenario,
        environment: SimulationEnvironment,
    ) -> list[EnterpriseEvent]:

        events = []

        for metric, value in scenario.effects.items():

            current_value = getattr(environment, metric)

            setattr(
                environment,
                metric,
                current_value + value,
            )

            event = EnterpriseEvent(
                event_type="STATE_CHANGE",
                source=scenario.name,
                description=f"{metric} changed by {value}",
                severity=EventSeverity.MEDIUM,
            )

            events.append(event)

        return events