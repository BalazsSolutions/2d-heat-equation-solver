2D Heat Equation Numerical Solver
A high-performance scientific computing project that solves the 2D Heat Equation using the Finite Difference Method in Python.
🚀 Visual Showcase

Key Features
Vectorized Architecture: No slow nested Python loops; entirely optimized using NumPy array slicing.
CFL Stability Enforcement: Automatically calculates and strictly enforces stability conditions.

Run the simulation
python main.py
📝 Mathematical Background
dT/dt = alpha * ( d^2T/dx^2 + d^2T/dy^2 )
