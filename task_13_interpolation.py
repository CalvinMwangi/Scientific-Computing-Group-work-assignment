import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Example: estimate electricity demand between recorded hours.
hours = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
demand_kw = np.array([2.1, 2.8, 3.6, 4.2, 4.0, 4.8, 5.3])

linear = interp1d(hours, demand_kw, kind="linear")
smooth = CubicSpline(hours, demand_kw)
fine_hours = np.linspace(6, 18, 100)

print(f"Estimated demand at 11:00 (linear): {float(linear(11)):.2f} kW")
print(f"Estimated demand at 11:00 (spline): {float(smooth(11)):.2f} kW")

# Parameter change: estimate at 13:00 instead of 11:00
print(f"Estimated demand at 13:00: {float(linear(13)):.2f} kW")

plt.scatter(hours, demand_kw, label="Recorded readings")
plt.plot(fine_hours, linear(fine_hours), label="Linear interpolation")
plt.plot(fine_hours, smooth(fine_hours), label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Electricity demand (kW)")
plt.title("Estimated electricity demand")
plt.legend()
plt.grid(True)
plt.show()
