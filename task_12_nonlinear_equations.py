import numpy as np
from scipy.optimize import root

# Example: intersection of a circular garden and a straight boundary.
# Circle: x^2 + y^2 = 25
# Line: y = x + 1
def equations(z):
    x, y = z
    return [x**2 + y**2 - 25, y - x - 1]

for starting_guess in ([2., 3.], [-4., -3.]):
    result = root(equations, starting_guess)
    print("Starting guess:", starting_guess)
    print("Intersection point:", result.x)
    print("Residuals:", equations(result.x))
    print("Solver successful:", result.success)
    print()

# Parameter change: use a larger circle of radius 6
def larger_circle(z):
    x, y = z
    return [x**2 + y**2 - 36, y - x - 1]

changed = root(larger_circle, [3., 4.])
print("Intersection for radius 6:", changed.x)
