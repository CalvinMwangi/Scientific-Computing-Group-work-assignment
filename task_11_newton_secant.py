from scipy.optimize import root_scalar

# Example: determine the production level where revenue equals cost.
# Profit(q) = q^2 - 7q - 30; the positive root is the break-even level.
def profit(q):
    return q**2 - 7*q - 30

def derivative(q):
    return 2*q - 7

newton = root_scalar(profit, fprime=derivative, x0=10, method="newton")
secant = root_scalar(profit, x0=8, x1=10, method="secant")

print(f"Break-even output (Newton): {newton.root:.6f} units")
print(f"Break-even output (Secant): {secant.root:.6f} units")
print(f"Profit at estimated root: {profit(newton.root):.8f}")

# Parameter change: increase fixed cost by 10
def changed_profit(q):
    return q**2 - 7*q - 40

changed = root_scalar(changed_profit, x0=10, fprime=derivative,
                      method="newton")
print("Break-even output with higher cost:", changed.root)
