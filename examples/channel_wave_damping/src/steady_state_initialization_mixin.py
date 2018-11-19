from rtctools.optimization.optimization_problem import OptimizationProblem


class SteadyStateInitializationMixin(OptimizationProblem):
    def constraints(self, ensemble_member):
        c = super().constraints(ensemble_member)
        times = self.times()
        parameters = self.parameters(ensemble_member)
        # Force steady-state initialization at t0 and at t1.
        for reach in ['upstream', 'middle', 'downstream']:
            # We skip the last level node as it needs to be free for the control law to
            # act upon.
            for i in range(int(parameters[f'{reach}.n_level_nodes']) - 1):
                state = f'{reach}.H[{i + 1}]'
                c.append(
                    (self.state_at(state, times[0]) - self.state_at(state, times[1]), 0, 0)
                )
            for i in range(int(parameters[f'{reach}.n_level_nodes']) + 1):
                state = f'{reach}.Q[{i + 1}]'
                c.append(
                    (self.der_at(state, times[0]), 0, 0)
                )
        return c
