import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Example: three connected water tanks with a fixed coefficient matrix.
A = np.array([[5.0, -1.0, 0.0],
              [-1.0, 4.0, -1.0],
              [0.0, -1.0, 3.0]])

# Several different supply/measurement conditions
right_sides = [
    np.array([12.0, 8.0, 7.0]),
    np.array([14.0, 7.0, 9.0]),
    np.array([10.0, 9.0, 8.0])
]

# Factorise A once, then reuse the factors
lu, pivots = lu_factor(A)
for number, b in enumerate(right_sides, start=1):
    answer = lu_solve((lu, pivots), b)
    print(f"Case {number}: solution = {answer}")
    print("Residual norm =", np.linalg.norm(A @ answer - b))

# Parameter change: solve another supply condition
new_b = np.array([15.0, 8.0, 6.0])
print("Changed condition solution:", lu_solve((lu, pivots), new_b))
