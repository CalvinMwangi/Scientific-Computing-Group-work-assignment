import numpy as np
import timeit

# Example: convert a batch of parcel weights from kg to grams
weights_kg = np.linspace(0.2, 25, 500_000)

def with_loop():
    result = []
    for weight in weights_kg:
        result.append(weight * 1000)
    return result

def with_numpy():
    return weights_kg * 1000

loop_seconds = timeit.timeit(with_loop, number=1)
numpy_seconds = timeit.timeit(with_numpy, number=5) / 5

grams = with_numpy()
print("First five weights in grams:", grams[:5])
print(f"Loop execution: {loop_seconds:.5f} seconds")
print(f"NumPy execution: {numpy_seconds:.5f} seconds")
print(f"Approximate speed ratio: {loop_seconds / numpy_seconds:.1f}x")

# Parameter change: increase the number of parcels to 1,000,000
larger_batch = np.linspace(0.2, 25, 1_000_000)
print("Larger batch size:", larger_batch.size)
print("Total weight in kg:", np.sum(larger_batch))
