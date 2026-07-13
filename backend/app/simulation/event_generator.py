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
        changes: dict,
    ) -> list[EnterpriseEvent]:

        events = []

        for metric, value in scenario.effects.items():

            event = EnterpriseEvent(
                enterprise_id="enterprise-001",
                scenario_id=scenario.id,

                event_type="STATE_CHANGE",
                metric=metric,

                previous_value=changes[metric]["previous"],
                current_value=changes[metric]["current"],

                severity=EventSeverity.MEDIUM,
                source="SimulationEngine",
                )

            events.append(event)

        return events