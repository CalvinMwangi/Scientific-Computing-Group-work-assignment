import numpy as np

# Example: connections between four university departments.
# The matrix records whether two departments collaborate.
network = np.array([[0., 1., 1., 0.],
                    [1., 0., 1., 1.],
                    [1., 1., 0., 1.],
                    [0., 1., 1., 0.]])

values, vectors = np.linalg.eig(network)
idx = np.argmax(np.real(values))
largest_value = np.real(values[idx])
importance = np.abs(np.real(vectors[:, idx]))
importance = importance / importance.sum()

departments = ["Computing", "Business", "Engineering", "Science"]
print("Largest eigenvalue:", largest_value)
for name, score in zip(departments, importance):
    print(f"{name}: importance score = {score:.4f}")

print("Verification error:",
      np.linalg.norm(network @ vectors[:, idx] -
                     largest_value * vectors[:, idx]))

# Parameter change: add a collaboration between departments 1 and 4
changed = network.copy()
changed[0, 3] = changed[3, 0] = 1
new_values, new_vectors = np.linalg.eig(changed)
print("Largest eigenvalue after new link:",
      np.max(np.real(new_values)))
