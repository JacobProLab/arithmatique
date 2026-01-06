import numpy as np
import matplotlib.pyplot as plt

# imagine a pile of (2) books of height (3) and width (3)
matrix_3d = np.array(
    [[np.random.choice(np.arange(20), size=3) for m in range(3)] for p in range(2)]
)
print(matrix_3d)

# Slicing
slice0 = matrix_3d[1, 2, 1]
slice1 = matrix_3d[:, :2, 1:2]
slice2 = matrix_3d[:, matrix_3d.shape[1] - 1]

# Applying function to all elements from an array
vectorized_add_100 = np.vectorize(lambda i: i + 100)
diffusion_add_100 = matrix_3d + 100
# (vectorized_add_100 == diffusion_add_100) = True

# min & max
max_value = np.max(matrix_3d)
min_value = np.min(matrix_3d)
max_d0_values = np.max(
    matrix_3d, axis=0
)  # returns max for dimension 0 (à la premiere "couche")
max_d1_values = np.max(
    matrix_3d, axis=1
)  # returns max for dimension 1 (à la deuxieme "couche")
max_d2_values = np.max(
    matrix_3d, axis=2
)  # returns max for dimension 2 (à la troisieme "couche")

# Descriptive statistics
mean = np.mean(matrix_3d)
variance = np.var(matrix_3d)
std = np.std(matrix_3d)
