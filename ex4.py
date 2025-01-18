from scipy.spatial import Voronoi, voronoi_plot_2d, ConvexHull
import numpy as np
import matplotlib.pyplot as plt

# Define the points Ai, Bi, Ci
A_points = [(1 - i, i - 1) for i in range(6)]
B_points = [(i, -i) for i in range(6)]
C_points = [(0, i) for i in range(6)]

# Combine all points
points = np.array(A_points + B_points + C_points)

# Compute the Voronoi diagram
vor = Voronoi(points)

# Count the number of half-lines (infinite edges)
half_lines_count = sum(1 for ridge in vor.ridge_vertices if -1 in ridge)

print(f"The number of half-lines in the Voronoi diagram is: {half_lines_count}")

# Compute the convex hull
hull = ConvexHull(points)

# Plot the Voronoi diagram
fig, ax = plt.subplots(figsize=(10, 8))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2)

# Plot the points
ax.plot(points[:, 0], points[:, 1], 'ro', label="Points")

# Plot the convex hull
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], 'green', linewidth=2)
    
ax.plot([], [], 'green', linewidth=2, label="Convex Hull")

# Add labels and grid
ax.set_title("Voronoi Diagram with Convex Hull")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend(loc='best')
plt.show()
