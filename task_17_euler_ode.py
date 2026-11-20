import numpy as np
import matplotlib.pyplot as plt

# Example: model the growth of a plant under ideal conditions.
# dH/dt = rH, where H is height in cm and r is growth rate per day.
initial_height = 5.0
growth_rate = 0.08
step = 0.5
days = 20

times = np.arange(0, days + step, step)
height = np.zeros_like(times)
height[0] = initial_height

for i in range(len(times) - 1):
    height[i+1] = height[i] + step * growth_rate * height[i]

exact = initial_height * np.exp(growth_rate * times)
print(f"Euler estimated height after {days} days: {height[-1]:.2f} cm")
print(f"Exact model height after {days} days: {exact[-1]:.2f} cm")
print(f"Absolute difference: {abs(height[-1]-exact[-1]):.4f} cm")

# Parameter change: use a smaller step size
small_step = 0.1
small_times = np.arange(0, days + small_step, small_step)
small_height = np.zeros_like(small_times)
small_height[0] = initial_height
for i in range(len(small_times)-1):
    small_height[i+1] = (small_height[i] +
                         small_step * growth_rate * small_height[i])
print("Estimate using 0.1-day step:", f"{small_height[-1]:.2f} cm")

plt.plot(times, height, "o-", label="Euler, step 0.5 day")
plt.plot(times, exact, "--", label="Exact model")
plt.xlabel("Days")
plt.ylabel("Plant height (cm)")
plt.title("Model of plant growth")
plt.legend()
plt.grid(True)
plt.show()
