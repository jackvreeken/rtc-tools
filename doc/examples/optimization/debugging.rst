Debugging an Optimization Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
--------

This example will illustrate a few tools that can help debugging an optimization problem.
For example, it will demonstrate how to test an optimization problem by only solving
for a fixed number of time steps.

A Basic Optimization Problem
----------------------------

For this example, the model is kept very basic.
We consider a single reservoir with a few target and optimization goals.
The optimization problem is given below.

.. literalinclude:: ../../../examples/single_reservoir/src/single_reservoir.py
  :language: python
  :pyobject: SingleReservoir

Optimizing for a given number of time steps
-------------------------------------------

The class attribute ``_number_of_timesteps_to_optimize`` indicates for how many time steps
the control variables will be optimized.
By default this value is ``None``,
which means that the variables will be optimized for all time steps.
By setting this attribute to, e.g. ``5``, the variables will be optimized
for only the first 5 time steps.
This can be useful to find out when a problem becomes infeasable.
By setting ``_number_of_timesteps_to_optimize`` to ``0``,
the variables will only be optimized for the initial time.
This can be useful to check if the optimization problem is infeasable
due to incompatible initial conditions.
