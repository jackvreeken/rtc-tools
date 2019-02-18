model ModelSymbolicParameters
	parameter Real w_seed;

	Real x(start=1.1, fixed=true);
	Real w(start=w_seed);

	parameter Real k = 1.0;

	parameter Real u_max;
	input Real u(fixed=false, min = -2, max = u_max);
equation
	der(x) = k * x + u;
	der(w) = x;
end ModelSymbolicParameters;