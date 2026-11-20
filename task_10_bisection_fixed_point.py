import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# Example: find the water level where a simple balance model is zero.
# f(h) = h^2 + 2h - 15
def balance(h):
    return h**2 + 2*h - 15

result = root_scalar(balance, bracket=[2, 4], method="bisect", xtol=1e-10)

# Fixed-point form: h = sqrt(15 - 2h)
def g(h):
    return np.sqrt(15 - 2*h)

h = 3.0
history = [h]
for _ in range(100):
    next_h = g(h)
    history.append(next_h)
    if abs(next_h - h) < 1e-10:
        break
    h = next_h

print(f"Bisection root: {result.root:.8f}")
print(f"Fixed-point estimate: {history[-1]:.8f}")
print("Fixed-point iterations:", len(history) - 1)

# Parameter change: solve a model with constant 18 instead of 15
changed = root_scalar(lambda x: x**2 + 2*x - 18,
                      bracket=[2, 4], method="bisect")
print("Root after changing 15 to 18:", changed.root)

x = np.linspace(0, 5, 200)
plt.plot(x, balance(x), label="h² + 2h - 15")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(result.root, linestyle="--", label="Estimated root")
plt.xlabel("Water level h")
plt.ylabel("Balance")
plt.title("Bisection root of the water-level model")
plt.legend()
plt.grid(True)
plt.show()
