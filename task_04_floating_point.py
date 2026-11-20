import numpy as np

# Example: rounding error in a measurement instrument
measured = 12.67891
displayed = round(measured, 2)
absolute_error = abs(measured - displayed)
relative_error = absolute_error / abs(measured)

print("Stored measurement:", measured)
print("Displayed measurement:", displayed)
print(f"Absolute error: {absolute_error:.5f}")
print(f"Relative error: {relative_error:.4%}")

# Floating-point values should be compared with a tolerance
a = 0.1 + 0.2
b = 0.3
print("Exact equality:", a == b)
print("Close within tolerance:", np.isclose(a, b))

# Parameter change: display 4 decimal places instead of 2
displayed_more_precisely = round(measured, 4)
print("With 4 decimal places:", displayed_more_precisely)
print("New absolute error:", abs(measured - displayed_more_precisely))
