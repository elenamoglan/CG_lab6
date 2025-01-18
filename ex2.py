import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d, ConvexHull

# Define the original points
original_points = np.array(
    [
        [5, -1],  # A1
        [7, -1],  # A2
        [9, -1],  # A3
        [7, -3],  # A4
        [11, -1],  # A5
        [-9, 3],  # A6
    ]
)

# Add the new points A7 and A8
new_points = np.array(
    [
        [-10, -5],  # A7
        [13, 5],  # A8
    ]
)

# Combine all points
all_points = np.vstack([original_points, new_points])

# Compute Voronoi Diagram
vor = Voronoi(all_points)

# Create a figure
fig, ax = plt.subplots(figsize=(8, 8))

# Plot Voronoi regions
voronoi_plot_2d(
    vor,
    ax=ax,
    show_vertices=False,
    line_colors="blue",
    line_width=1.5,
    line_alpha=0.6,
    point_size=2,
)

# Highlight Voronoi regions with filled color
for region_index in vor.regions:
    if not -1 in region_index and len(region_index) > 0:  # Skip unbounded regions
        polygon = [vor.vertices[i] for i in region_index]
        ax.fill(*zip(*polygon), color="blue", alpha=0.1)

# Plot points
ax.scatter(all_points[:, 0], all_points[:, 1], color="red", zorder=5)

# Annotate points
labels = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
for i, (x, y) in enumerate(all_points):
    ax.text(x, y, labels[i], verticalalignment="bottom", horizontalalignment="right")

# Compute and plot Convex Hull
hull = ConvexHull(all_points)
for simplex in hull.simplices:
    ax.plot(all_points[simplex, 0], all_points[simplex, 1], "g-", linewidth=2)

# Add legend
ax.legend(["Voronoi Regions", "Points", "Convex Hull"], loc="best")

# Add labels and title
ax.set_title("Voronoi Diagram with Exactly 4 Half-Line Edges")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis("equal")
ax.set_xlim(
    np.min(all_points[:, 0]) - 2, np.max(all_points[:, 0]) + 2
)  # Set x-axis limits
ax.set_ylim(
    np.min(all_points[:, 1]) - 2, np.max(all_points[:, 1]) + 2
)  # Set y-axis limits
ax.grid()

# Show the plot
plt.show()
