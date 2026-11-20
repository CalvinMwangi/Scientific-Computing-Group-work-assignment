import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Example: model medicine concentration leaving a simplified system.
# dC/dt = -kC
initial_concentration = 80.0
decay_rate = 0.18

def concentration_model(t, concentration):
    return [-decay_rate * concentration[0]]

sample_times = np.linspace(0, 24, 150)
solution = solve_ivp(concentration_model, (0, 24),
                     [initial_concentration], t_eval=sample_times)

exact = initial_concentration * np.exp(-decay_rate * solution.t)
print("Solver successful:", solution.success)
print(f"Concentration after 24 hours: {solution.y[0, -1]:.3f}")
print(f"Maximum numerical error: "
      f"{np.max(np.abs(solution.y[0]-exact)):.3e}")

# Parameter change: faster decay rate
decay_rate = 0.25
faster = solve_ivp(concentration_model, (0, 24),
                   [initial_concentration], t_eval=sample_times)
print(f"After changing decay rate, final concentration: {faster.y[0,-1]:.3f}")

plt.plot(solution.t, solution.y[0], label="Original rate")
plt.plot(faster.t, faster.y[0], label="Higher decay rate")
plt.xlabel("Time (hours)")
plt.ylabel("Model concentration (arbitrary units)")
plt.title("Numerical solution of a decay differential equation")
plt.legend()
plt.grid(True)
plt.show()
