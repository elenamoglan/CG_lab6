% Define the points A, B, and C
A = [1 - (0:5); (0:5) - 1]';       % Points A0 to A5
B = [(0:5)', -(0:5)'];             % Points B0 to B5
C = [zeros(6,1), (0:5)'];          % Points C0 to C5

% Combine all points into a single set
points = [A; B; C];

% Remove duplicate points
points = unique(points, 'rows');

% Compute Voronoi diagram
[vx, vy] = voronoi(points(:,1), points(:,2));

% Compute convex hull
k = convhull(points(:,1), points(:,2));
convex_hull_points = points(k, :);

% Create a single figure
figure;

% Plot the Voronoi diagram
plot(vx, vy, 'b-'); % Voronoi edges in blue
hold on;

% Plot all points
scatter(points(:,1), points(:,2), 50, 'filled', 'k'); % Points in black

% Plot the convex hull
plot(convex_hull_points(:,1), convex_hull_points(:,2), 'r-', 'LineWidth', 2); % Convex hull in red

% Add titles and labels
title('Voronoi Diagram with Convex Hull');
xlabel('X');
ylabel('Y');
axis equal;
grid;

% Highlight convex hull points
scatter(convex_hull_points(:,1), convex_hull_points(:,2), 70, 'filled', 'r'); % Convex hull vertices in red
hold off;

% Display number of half-lines
num_half_lines = length(k) - 1;  % Remove duplicate closing point
x = sprintf('Number of half-lines in the Voronoi diagram: %d', num_half_lines);
disp(x);
