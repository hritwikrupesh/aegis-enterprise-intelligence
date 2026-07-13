from app.domain.entities.enterprise_event import EnterpriseEvent
from app.domain.entities.scenario import Scenario
from app.domain.enums.event_severity import EventSeverity
from app.simulation.environment import SimulationEnvironment


class EventGenerator:
    """
    Generates enterprise events after the environment
    has already been updated.
    """

    def generate(
        self,
        scenario: Scenario,
        environment: SimulationEnvironment,
    ) -> list[EnterpriseEvent]:

        events = []

        for metric, value in scenario.effects.items():

            event = EnterpriseEvent(
                event_type="STATE_CHANGE",
                source=scenario.name,
                description=f"{metric} changed by {value}",
                severity=EventSeverity.MEDIUM,
            )

            events.append(event)

        return events