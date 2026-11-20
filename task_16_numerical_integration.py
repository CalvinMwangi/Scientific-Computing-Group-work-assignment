import numpy as np
from scipy.integrate import simpson

# Example: estimate water pumped by a system from flow-rate readings.
time_minutes = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)
flow_litres_min = np.array([4.0, 4.5, 5.2, 5.8, 5.5, 4.9, 4.2])

volume_trapezoid = np.trapezoid(flow_litres_min, time_minutes)
volume_simpson = simpson(flow_litres_min, x=time_minutes)

print(f"Volume by trapezoidal rule: {volume_trapezoid:.2f} litres")
print(f"Volume by Simpson's rule: {volume_simpson:.2f} litres")
print(f"Difference: {abs(volume_simpson-volume_trapezoid):.3f} litres")

# Parameter change: calculate only the first 20 minutes
partial_volume = np.trapezoid(flow_litres_min[:5], time_minutes[:5])
print(f"Estimated volume in first 20 minutes: {partial_volume:.2f} litres")
