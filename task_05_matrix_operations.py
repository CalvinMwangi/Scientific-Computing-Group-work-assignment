import numpy as np

# Example: a shop sells three products in two branches.
# Rows represent branches; columns represent products.
sales = np.array([[12, 8, 15],
                  [10, 11, 9]])
prices = np.array([250, 400, 150])

branch_revenue = sales @ prices
print("Sales matrix:\n", sales)
print("Revenue for each branch (KES):", branch_revenue)
print("Total revenue (KES):", np.sum(branch_revenue))

# Scale all sales quantities by 10% to model increased demand
increased_sales = sales * 1.10
print("Projected revenue after 10% increase (KES):",
      increased_sales @ prices)

# Matrix determinant example
matrix = np.array([[3, 1], [2, 4]])
print("Determinant:", np.linalg.det(matrix))
