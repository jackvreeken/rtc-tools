from rtctools.optimization.collocated_integrated_optimization_problem import (
    CollocatedIntegratedOptimizationProblem)
from rtctools.optimization.csv_mixin import CSVMixin
from rtctools.optimization.goal_programming_mixin import (
    Goal,
    GoalProgrammingMixin)
from rtctools.optimization.modelica_mixin import ModelicaMixin
from rtctools.util import run_optimization_problem


class VolumeRangeGoal(Goal):
    def function(self, optimization_problem, ensemble_member):
        del ensemble_member
        return optimization_problem.state('V_storage')

    function_range = [0, 25e3]
    target_min = 10e3
    target_max = 20e3
    priority = 1


class MinimizeQpumpGoal(Goal):
    def function(self, optimization_problem, ensemble_member):
        del ensemble_member
        return optimization_problem.integral('Q_release')

    function_nominal = 1.0
    priority = 2


class MinimizeChangeInQpumpGoal(Goal):
    def function(self, optimization_problem, ensemble_member):
        del ensemble_member
        return optimization_problem.der('Q_release')

    function_nominal = 1e-3
    priority = 3
    order = 2


class SingleReservoir(
    GoalProgrammingMixin,
    CSVMixin,
    ModelicaMixin,
    CollocatedIntegratedOptimizationProblem
):
    """
    An optimization problem involving a single reservoir.
    """

    def path_constraints(self, ensemble_member):
        constraints = super().path_constraints(ensemble_member)
        constraints.append((self.state('Q_release'), 0, 1.5))
        return constraints

    def goals(self):
        return [
            MinimizeQpumpGoal()]

    def path_goals(self):
        return [
            VolumeRangeGoal(),
            MinimizeChangeInQpumpGoal()]


# Run
run_optimization_problem(SingleReservoir)
