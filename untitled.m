% Define points
points = [3, -5;    % A
          -6, 6;    % B
           6, -4;   % C
           5, -5;   % D
           9, 10];  % E

% Compute Delaunay Triangulation
tri = delaunay(points(:,1), points(:,2));

% Create a larger figure
figure('Position', [100, 100, 1200, 600]); % Adjust size as needed

% Plot Delaunay Triangulation
subplot(1, 2, 1, 'Position', [0.05, 0.1, 0.4, 0.8]); % [left, bottom, width, height]
triplot(tri, points(:,1), points(:,2), 'g');
hold on;
scatter(points(:,1), points(:,2), 'ro', 'filled');
labels = {'A', 'B', 'C', 'D', 'E'};
for i = 1:length(points)
    text(points(i,1), points(i,2), labels{i}, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
end
title('Delaunay Triangulation');
grid;
hold off;

% Compute Voronoi Diagram
[vx, vy] = voronoi(points(:,1), points(:,2));

% Plot Voronoi Diagram
subplot(1, 2, 2, 'Position', [0.55, 0.1, 0.4, 0.8]); % [left, bottom, width, height]
plot(vx, vy, 'b');
hold on;
scatter(points(:,1), points(:,2), 'ro', 'filled');
for i = 1:length(points)
    text(points(i,1), points(i,2), labels{i}, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
end
title('Voronoi Diagram');
grid;
hold off;
