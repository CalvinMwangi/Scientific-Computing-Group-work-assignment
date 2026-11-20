# BIT 2118 – Scientific Computing (Alternative Examples)

This project contains original Python examples for Tasks 2–20. The examples follow the topics in the supplied assignment brief but use different scenarios and input values from the reference document.

## Requirements
- Python 3.10 or later
- NumPy
- SciPy
- Matplotlib

Install the libraries in the VS Code terminal:

```bash
python -m pip install -r requirements.txt
```

## Running a task
Open the project folder in VS Code. Open the `code` folder, select a task file, and run it using the Run Python File button or:

```bash
python code/task_02_numpy_arrays.py
```

For tasks that create a graph, a plot window will appear. Close it to finish the program.

## Task guide

| Task | Topic | Example used | Main operation |
|---|---|---|---|
| 2 | NumPy arrays | Smart-meter water readings | Mean, minimum, maximum and unit conversion |
| 3 | Vectorization | Parcel weights | Array multiplication and timing comparison |
| 4 | Floating-point errors | Instrument measurement | Absolute/relative error and tolerance comparison |
| 5 | Matrix operations | Shop sales in two branches | Matrix-vector multiplication and determinant |
| 6 | Linear equations | Fruit basket production | Solve Ax = b |
| 7 | Gaussian elimination and LU | Water-tank model | LU factorisation and repeated solves |
| 8 | Iterative methods | Metal-bar temperatures | Jacobi iteration and convergence |
| 9 | Eigenvalues/eigenvectors | Department collaboration network | Eigen decomposition and importance scores |
| 10 | Bisection/fixed point | Water-level balance | Root finding |
| 11 | Newton-Raphson/secant | Production break-even point | Numerical root estimation |
| 12 | Nonlinear equations | Garden-circle and line intersection | Nonlinear system solver |
| 13 | Interpolation | Electricity demand | Linear and cubic interpolation |
| 14 | Curve fitting | Advertising and sales | Least-squares model fitting |
| 15 | Numerical differentiation | Cyclist distance readings | Numerical gradient |
| 16 | Numerical integration | Pumped water | Trapezoidal and Simpson rules |
| 17 | Euler method | Plant growth | Forward Euler ODE approximation |
| 18 | SciPy ODE solver | Exponential concentration decay model | `solve_ivp` |
| 19 | Optimization | Product mix under a budget | Constrained minimization |
| 20 | Monte Carlo | Stock-shortage probability | Random sampling and probability estimate |

## How the assignment requirements are addressed
Each script identifies its input values, performs the mathematical operation, prints results, and changes at least one parameter so the effect can be observed. Where appropriate, the program also displays a graph. The scenarios are alternative practice cases; use the printed results from your own run when writing your interpretation.

## Suggested individual GitHub repository structure

```text
BIT2118-Scientific-Computing/
├── README.md
├── requirements.txt
└── code/
    ├── task_02_numpy_arrays.py
    ├── ...
    └── task_20_monte_carlo.py
```

## Important submission note
The assignment brief says discussions may be done as a group, but each student must maintain and submit an individual GitHub repository. Add your own explanations, screenshots of actual program output, and your own modified real-world case for each required task before submitting. Do not submit another student's repository as your own.
