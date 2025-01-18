import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

import matplotlib.pyplot as plt

# Define the sets of points
M1 = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2], [0.5, np.sqrt(3) / 6]])
M2 = np.array(
    [
        [0, 0],
        [1, 0],
        [0.5, np.sqrt(3) / 2],
        [0.5, np.sqrt(3) / 6],
        [0.75, np.sqrt(3) / 4],
    ]
)

# Triangulate the points
tri_M1 = Delaunay(M1)
tri_M2 = Delaunay(M2)

# Voronoi diagrams
vor_M1 = Voronoi(M1)
vor_M2 = Voronoi(M2)

# Plotting the triangulations and Voronoi diagrams
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Triangulation for M1
axs[0, 0].triplot(M1[:, 0], M1[:, 1], tri_M1.simplices)
axs[0, 0].plot(M1[:, 0], M1[:, 1], "o")
axs[0, 0].set_title("Triangulation of M1")

# Triangulation for M2
axs[0, 1].triplot(M2[:, 0], M2[:, 1], tri_M2.simplices)
axs[0, 1].plot(M2[:, 0], M2[:, 1], "o")
axs[0, 1].set_title("Triangulation of M2")

# Voronoi diagram for M1
voronoi_plot_2d(vor_M1, ax=axs[1, 0])
axs[1, 0].plot(M1[:, 0], M1[:, 1], "o")
axs[1, 0].set_title("Voronoi Diagram of M1")

# Voronoi diagram for M2
voronoi_plot_2d(vor_M2, ax=axs[1, 1])
axs[1, 1].plot(M2[:, 0], M2[:, 1], "o")
axs[1, 1].set_title("Voronoi Diagram of M2")

plt.show()

# Number of edges in the triangulations
num_edges_M1 = len(tri_M1.convex_hull) + len(tri_M1.simplices)
num_edges_M2 = len(tri_M2.convex_hull) + len(tri_M2.simplices)

# Number of half-line edges in the Voronoi diagrams
num_half_line_edges_M1 = sum(1 for region in vor_M1.regions if -1 in region)
num_half_line_edges_M2 = sum(1 for region in vor_M2.regions if -1 in region)

print(f"Number of edges in the triangulation of M1: {num_edges_M1}")
print(f"Number of edges in the triangulation of M2: {num_edges_M2}")
print(
    f"Number of half-line edges in the Voronoi diagram of M1: {num_half_line_edges_M1}"
)
print(
    f"Number of half-line edges in the Voronoi diagram of M2: {num_half_line_edges_M2}"
)
