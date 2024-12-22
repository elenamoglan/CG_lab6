% Define the points
A = [1, 1];
B = [1, -1];
C = [-1, -1];
D = [-1, 1];
E = [0, -2];
lambda = 0; % Set lambda value for M
M = [0, lambda];

points = [A; B; C; D; E; M];

% Perform Delaunay triangulation
tri = delaunay(points(:, 1), points(:, 2));

% Number of triangles
num_triangles = size(tri, 1);

% Count edges
edges = [];
for i = 1:num_triangles
    edges = [edges; sort([tri(i, 1), tri(i, 2)]); 
                   sort([tri(i, 2), tri(i, 3)]); 
                   sort([tri(i, 3), tri(i, 1)])];
end

% Remove duplicate edges
edges = unique(edges, 'rows');

% Number of edges
num_edges = size(edges, 1);

% Display results
fprintf('Number of triangles: %d\n', num_triangles);
fprintf('Number of edges: %d\n', num_edges);

% Plot the points and filled triangles
figure;
hold on;

% Plot filled triangles
colors = lines(num_triangles); % Generate colors
for i = 1:num_triangles
    fill(points(tri(i, :), 1), points(tri(i, :), 2), colors(i, :), 'FaceAlpha', 0.5, 'EdgeColor', 'k');
end

% Plot points
scatter(points(:, 1), points(:, 2), 100, 'r', 'filled'); % Plot points
text(points(:, 1) + 0.1, points(:, 2), {'A', 'B', 'C', 'D', 'E', 'M'}, 'FontSize', 12);

hold off;
axis equal;
title('Delaunay Triangulation with Filled Triangles');
xlabel('x');
ylabel('y');
grid on;
