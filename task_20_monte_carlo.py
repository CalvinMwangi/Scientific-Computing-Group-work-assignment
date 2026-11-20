import numpy as np
import matplotlib.pyplot as plt

# Example: estimate the chance that daily customer demand exceeds stock.
rng = np.random.default_rng(21)
stock_available = 500
average_demand = 430
demand_std = 70
number_of_trials = 100_000

daily_demand = rng.normal(average_demand, demand_std, number_of_trials)
shortage = daily_demand > stock_available
estimated_probability = np.mean(shortage)

print(f"Estimated shortage probability: {estimated_probability:.2%}")
print(f"Shortage cases: {np.sum(shortage)} out of {number_of_trials}")

# Parameter change: increase stock availability
more_stock = 550
shortage_more_stock = daily_demand > more_stock
print(f"Probability with stock of {more_stock}: "
      f"{np.mean(shortage_more_stock):.2%}")

running_estimate = np.cumsum(shortage) / np.arange(1, number_of_trials + 1)
indices = np.unique(np.logspace(1, np.log10(number_of_trials), 200).astype(int)) - 1

plt.semilogx(indices + 1, running_estimate[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated shortage probability")
plt.title("Monte Carlo estimate as simulations increase")
plt.grid(True)
plt.show()
