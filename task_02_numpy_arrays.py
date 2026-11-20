import numpy as np

# Example: daily water use recorded by a smart meter (litres)
water_litres = np.array([120, 135, 128, 142, 150, 138, 145, 155])

print("Daily readings:", water_litres)
print(f"Average use: {np.mean(water_litres):.2f} litres")
print(f"Lowest use: {np.min(water_litres)} litres")
print(f"Highest use: {np.max(water_litres)} litres")

# Convert litres to cubic metres (1 m3 = 1000 litres)
water_m3 = water_litres / 1000
print("Readings in cubic metres:", water_m3)

# Parameter change: add a higher reading and compare the average
changed = np.append(water_litres, 200)
print(f"New average after adding 200 L: {np.mean(changed):.2f} litres")
