from scipy.optimize import minimize

# Example: choose quantities of two products to maximise income
# while staying within a limited production budget.
# Minimise negative income because scipy.optimize.minimize performs minimisation.
def negative_income(z):
    product_a, product_b = z
    return -(40*product_a + 55*product_b)

def budget_limit(z):
    product_a, product_b = z
    return 1000 - (20*product_a + 35*product_b)

constraints = [{"type": "ineq", "fun": budget_limit}]
bounds = [(0, None), (0, None)]

result = minimize(negative_income, x0=[10, 10],
                  method="SLSQP", bounds=bounds,
                  constraints=constraints)

a, b = result.x
print("Optimization successful:", result.success)
print(f"Product A quantity: {a:.2f}")
print(f"Product B quantity: {b:.2f}")
print(f"Budget used: {20*a + 35*b:.2f}")
print(f"Maximum estimated income: {-result.fun:.2f}")

# Parameter change: increase available budget from 1000 to 1200
def larger_budget(z):
    return 1200 - (20*z[0] + 35*z[1])

changed = minimize(negative_income, x0=[10, 10],
                   method="SLSQP", bounds=bounds,
                   constraints=[{"type": "ineq", "fun": larger_budget}])
print("Maximum income with larger budget:", -changed.fun)
