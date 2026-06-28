2D Heat Equation (PDE) Numerical Solver
A high-performance scientific computing project that solves the 2D Heat Equation (Partial Differential Equation) using the Finite Difference Method with a Forward-Time Central-Space (FTCS) scheme in Python.
The solver leverages vectorized matrix operations via NumPy for speed and features a beautiful dark-themed real-time animation built with Matplotlib.
🚀 Visual Showcase
Behold the physical simulation of heat diffusion over time. The system initializes with a cool baseline, constant boundary conditions on the walls, and a Gaussian "hot spot" in the exact center:

✨ Key Features
Vectorized Architecture: No slow nested Python loops over grid points; entirely optimized using NumPy array slicing.
CFL Stability Enforcement: Automatically calculates and strictly enforces the Courant-Friedrichs-Lewy (CFL) condition for 2D diffusion to guarantee mathematical convergence and prevent simulation blow-up.
Gaussian Initialization: Generates a realistic, smooth heat distribution at the core using exponential spatial functions.
Production-Ready Visualization: Outfitted with an elegant dark theme (#0d0d0d), unified physics units, and a dynamic colorbar capturing temperature shifts up to 210°C.
🛠️ Tech Stack, Setup & Execution
1. Clone this repository
git clone https://github.com/BalazsSolutions/2d-heat-equation-solver.git
cd 2d-heat-equation-solver
2. Install the required dependencies
pip install numpy matplotlib
3. Run the simulation script
python main.py
📝 Mathematical Background
The script solves the classic 2D heat conduction equation:
dT/dt = alpha * ( d^2T/dx^2 + d^2T/dy^2 )

Using numerical discretization, the next time step is explicitly computed from the spatial laplacian of the current step, maintaining a strict safe bound bounded by the safety factor parameter.
