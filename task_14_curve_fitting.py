import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Example: relate advertising expenditure to weekly sales.
advertising = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)  # KES thousands
sales = np.array([12, 16, 21, 25, 31, 34, 40], dtype=float)  # units hundreds

def linear_model(x, slope, intercept):
    return slope*x + intercept

parameters, covariance = curve_fit(linear_model, advertising, sales)
slope, intercept = parameters
predicted = linear_model(advertising, slope, intercept)
rmse = np.sqrt(np.mean((sales - predicted)**2))

print(f"Fitted model: sales = {slope:.3f}*advertising + {intercept:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"Predicted sales at KES 8,000 advertising: "
      f"{linear_model(8, slope, intercept):.2f} hundreds")

# Parameter change: estimate for KES 10,000
print("Prediction at KES 10,000:",
      linear_model(10, slope, intercept), "hundreds")

x_line = np.linspace(1, 10, 100)
plt.scatter(advertising, sales, label="Observed data")
plt.plot(x_line, linear_model(x_line, *parameters), label="Fitted line")
plt.xlabel("Advertising expenditure (KES thousands)")
plt.ylabel("Weekly sales (hundreds of units)")
plt.title("Advertising and sales curve fitting")
plt.legend()
plt.grid(True)
plt.show()
