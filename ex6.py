import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import random

# Define the points
A = (1, 1)
B = (1, -1)
C = (-1, -1)
D = (-1, 1)
E = (0, -2)
lambda_value = random.randint(-10, 10) 
M = (0, lambda_value)

points = np.array([A, B, C, D, E, M])

# Perform Delaunay triangulation
tri = Delaunay(points)

# Number of triangles
num_triangles = len(tri.simplices)

# Number of edges
edges = set()
for simplex in tri.simplices:
    for i in range(3):
        edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
        edges.add(edge)
num_edges = len(edges)

print(f"Random lambda value: {lambda_value}")
print(f"Number of triangles: {num_triangles}")
print(f"Number of edges: {num_edges}")

# Plotting the triangulation
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.title('Delaunay Triangulation')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()