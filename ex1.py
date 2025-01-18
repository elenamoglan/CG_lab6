import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

# Define points
points = np.array(
    [
        [3, -5],  # A
        [-6, 6],  # B
        [6, -4],  # C
        [5, -5],  # D
        [9, 10],  # E
    ]
)
labels = ["A", "B", "C", "D", "E"]

# Compute Delaunay Triangulation
delaunay = Delaunay(points)

# Create a larger figure
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot Delaunay Triangulation
axes[0].triplot(points[:, 0], points[:, 1], delaunay.simplices, "g-")
axes[0].scatter(points[:, 0], points[:, 1], c="red", zorder=5)
for i, (x, y) in enumerate(points):
    axes[0].text(
        x, y, labels[i], verticalalignment="bottom", horizontalalignment="right"
    )
axes[0].set_title("Delaunay Triangulation")
axes[0].grid()

# Compute Voronoi Diagram
vor = Voronoi(points)

# Plot Voronoi Diagram
voronoi_plot_2d(
    vor, ax=axes[1], show_vertices=False, line_colors="blue", line_width=1.5
)
axes[1].scatter(points[:, 0], points[:, 1], c="red", zorder=5)
for i, (x, y) in enumerate(points):
    axes[1].text(
        x, y, labels[i], verticalalignment="bottom", horizontalalignment="right"
    )
axes[1].set_title("Voronoi Diagram")
axes[1].grid()

# Adjust layout and show plot
plt.tight_layout()
plt.show()
