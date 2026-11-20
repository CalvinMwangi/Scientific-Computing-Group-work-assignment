import numpy as np

# A farm sells small and large fruit baskets.
# x = small baskets, y = large baskets.
# 2x + 3y =  thirty items of fruit;  x + 2y = 18 packing units.
A = np.array([[2.0, 3.0],
              [1.0, 2.0]])
b = np.array([30.0, 18.0])

quantities = np.linalg.solve(A, b)
print(f"Small baskets (x): {quantities[0]:.2f}")
print(f"Large baskets (y): {quantities[1]:.2f}")
print("Check A @ x:", A @ quantities)
print("Residual:", b - A @ quantities)

# Parameter change: increase the first total from 30 to 33
b_changed = np.array([33.0, 18.0])
changed_solution = np.linalg.solve(A, b_changed)
print("New quantities after changing first total:", changed_solution)
