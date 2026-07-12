import operator

from app.domain.entities.business_rule import BusinessRule
from app.simulation.environment import SimulationEnvironment


class RuleEngine:
    """
    Evaluates business rules and updates the simulation environment.
    """

    OPERATORS = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
    }

    def apply_rule(
        self,
        rule: BusinessRule,
        environment: SimulationEnvironment,
    ) -> None:

        current_value = getattr(environment, rule.metric)

        if self.OPERATORS[rule.operator](
            current_value,
            rule.threshold,
        ):

            current_target = getattr(
                environment,
                rule.target,
            )

            setattr(
                environment,
                rule.target,
                current_target + rule.adjustment,
            )