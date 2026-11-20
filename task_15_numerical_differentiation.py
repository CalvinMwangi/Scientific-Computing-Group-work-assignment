import numpy as np
import matplotlib.pyplot as plt

# Example: estimate a cyclist's speed from distance readings.
time_s = np.array([0, 2, 4, 6, 8, 10], dtype=float)
distance_m = np.array([0, 7, 17, 30, 46, 65], dtype=float)

speed = np.gradient(distance_m, time_s)
for t, d, v in zip(time_s, distance_m, speed):
    print(f"Time={t:>4.0f}s, distance={d:>5.1f}m, estimated speed={v:.2f}m/s")

# Parameter change: calculate average speed over the full period
average_speed = (distance_m[-1] - distance_m[0]) / (time_s[-1] - time_s[0])
print(f"Average speed over full journey: {average_speed:.2f} m/s")

plt.plot(time_s, speed, marker="o")
plt.xlabel("Time (seconds)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Cyclist speed estimated from distance readings")
plt.grid(True)
plt.show()
