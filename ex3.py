import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

# Define the points
points = np.array(
    [
        [-1, 6],  # A
        [-1, -1],  # B
        [4, 7],  # C
        [6, 7],  # D
        [1, -1],  # E
        [-5, 3],  # F
        [-2, 3],  # P
    ]
)

# Define the parameterized point Q
lambda_values = np.linspace(-10, 10, 1000)  # Range of lambda for evaluation
min_mst_length = np.inf  # Initialize the minimum MST length
optimal_lambda = None  # To store the optimal lambda

for lambda_val in lambda_values:
    # Compute Q based on lambda
    Q = np.array([2 - lambda_val, 3])

    # Add Q to the points list
    all_points = np.vstack([points, Q])

    # Compute the distance matrix
    dist_matrix = distance_matrix(all_points, all_points)

    # Compute the Minimum Spanning Tree (MST) length
    mst = minimum_spanning_tree(dist_matrix)
    mst_length = mst.sum()

    # Update the minimum MST length and optimal lambda
    if mst_length < min_mst_length:
        min_mst_length = mst_length
        optimal_lambda = lambda_val

# Display the result
print(f"Optimal lambda: {optimal_lambda:.4f}")
print(f"Minimum MST length: {min_mst_length:.4f}")

# Plot MST and points for the optimal lambda
optimal_Q = np.array([2 - optimal_lambda, 3])
all_points_optimal = np.vstack([points, optimal_Q])

# Recompute the distance matrix for the optimal lambda
dist_matrix_optimal = distance_matrix(all_points_optimal, all_points_optimal)
mst_optimal = minimum_spanning_tree(dist_matrix_optimal)

# Plot the MST and points
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the MST
for i, j in zip(*mst_optimal.nonzero()):
    x_coords = [all_points_optimal[i, 0], all_points_optimal[j, 0]]
    y_coords = [all_points_optimal[i, 1], all_points_optimal[j, 1]]
    ax.plot(x_coords, y_coords, "b-", linewidth=2)

# Plot the points
ax.scatter(all_points_optimal[:, 0], all_points_optimal[:, 1], color="red", zorder=5)

# Annotate points
labels = ["A", "B", "C", "D", "E", "F", "P", "Q"]
for i, (x, y) in enumerate(all_points_optimal):
    ax.text(x, y, labels[i], verticalalignment="bottom", horizontalalignment="right")

# Add labels and title
ax.set_title(f"MST for Optimal Lambda ({optimal_lambda:.4f})")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis("equal")
ax.grid()

# Show the plot
plt.show()
