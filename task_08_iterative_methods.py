import numpy as np
import matplotlib.pyplot as plt

# Example: steady temperatures at four points along a metal bar.
A = np.array([[4., -1., 0., 0.],
              [-1., 4., -1., 0.],
              [0., -1., 4., -1.],
              [0., 0., -1., 4.]])
b = np.array([80., 20., 20., 40.])

def jacobi(A, b, tolerance=1e-8, max_iterations=500):
    x = np.zeros_like(b)
    D = np.diag(A)
    R = A - np.diagflat(D)
    errors = []
    for _ in range(max_iterations):
        next_x = (b - R @ x) / D
        error = np.linalg.norm(next_x - x, ord=np.inf)
        errors.append(error)
        x = next_x
        if error < tolerance:
            break
    return x, errors

answer, errors = jacobi(A, b)
print("Estimated temperatures:", answer)
print("Iterations:", len(errors))
print("Direct solution for checking:", np.linalg.solve(A, b))

# Parameter change: a stricter tolerance generally needs more iterations
accurate_answer, accurate_errors = jacobi(A, b, tolerance=1e-11)
print("Iterations with stricter tolerance:", len(accurate_errors))

plt.semilogy(errors, label="Tolerance 1e-8")
plt.semilogy(accurate_errors, label="Tolerance 1e-11")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Jacobi method convergence")
plt.legend()
plt.grid(True)
plt.show()
