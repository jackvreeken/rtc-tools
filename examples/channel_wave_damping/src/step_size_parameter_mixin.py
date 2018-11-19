from rtctools.optimization.optimization_problem import OptimizationProblem


class StepSizeParameterMixin(OptimizationProblem):
    def parameters(self, ensemble_member):
        p = super().parameters(ensemble_member)
        times = self.times()
        p['step_size'] = times[1] - times[0]
        return p
