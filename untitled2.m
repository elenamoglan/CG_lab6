% Define the original points
original_points = [5, -1;    % A1
                   7, -1;    % A2
                   9, -1;    % A3
                   7, -3;    % A4
                   11, -1;   % A5
                   -9, 3];   % A6

% Add the new points A7 and A8
new_points = [-10, -5;  % A7
              13, 5];   % A8

% Combine all points
all_points = [original_points; new_points];

% Compute Voronoi Diagram
[v, c] = voronoin(all_points);

% Create a figure
figure;

% Plot Voronoi Edges
hold on;
for i = 1:length(c)
    if all(c{i} ~= 1) % Skip unbounded regions
        fill(v(c{i}, 1), v(c{i}, 2), 'b', 'FaceAlpha', 0.1, 'EdgeColor', 'blue'); % Voronoi Regions
    end
end

% Plot Points
h_points = scatter(all_points(:,1), all_points(:,2), 50, 'r', 'filled');

% Annotate Points
labels = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'};
for i = 1:size(all_points, 1)
    text(all_points(i,1), all_points(i,2), labels{i}, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
end

% Compute and Plot Convex Hull
K = convhull(all_points(:,1), all_points(:,2));
h_convex = plot(all_points(K,1), all_points(K,2), 'g-', 'LineWidth', 2); % Convex hull edges

% Dummy handle for Voronoi Regions legend
h_voronoi = plot(nan, nan, 'b-', 'LineWidth', 2);

% Add Legend
legend([h_voronoi, h_points, h_convex], ...
       {'Voronoi Regions', 'Points', 'Convex Hull'}, ...
       'Location', 'bestoutside');

% Add Labels and Title
title('Voronoi Diagram with Exactly 4 Half-Line Edges');
xlabel('X');
ylabel('Y');
axis equal;
hold off;
% Define the original points
original_points = [5, -1;    % A1
                   7, -1;    % A2
                   9, -1;    % A3
                   7, -3;    % A4
                   11, -1;   % A5
                   -9, 3];   % A6

% Add the new points A7 and A8
new_points = [-10, -5;  % A7
              13, 5];   % A8

% Combine all points
all_points = [original_points; new_points];

% Compute Voronoi Diagram
[v, c] = voronoin(all_points);

% Create a figure
figure;

% Plot Voronoi Edges
h1 = plot(vx, vy, 'b-', 'LineWidth', 1.5); % Voronoi edges
hold on;
for i = 1:length(c)
    if all(c{i} ~= 1) % Skip unbounded regions
        fill(v(c{i}, 1), v(c{i}, 2), 'b', 'FaceAlpha', 0.1, 'EdgeColor', 'blue'); % Voronoi Regions
    end
end

% Plot Points
h_points = scatter(all_points(:,1), all_points(:,2), 50, 'r', 'filled');

% Annotate Points
labels = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'};
for i = 1:size(all_points, 1)
    text(all_points(i,1), all_points(i,2), labels{i}, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
end

% Compute and Plot Convex Hull
K = convhull(all_points(:,1), all_points(:,2));
h_convex = plot(all_points(K,1), all_points(K,2), 'g-', 'LineWidth', 2); % Convex hull edges

% Dummy handle for Voronoi Regions legend
h_voronoi = plot(nan, nan, 'b-', 'LineWidth', 2);

% Add Legend
legend([h_voronoi, h_points, h_convex], ...
       {'Voronoi Regions', 'Points', 'Convex Hull'}, ...
       'Location', 'bestoutside');

% Add Labels and Title
title('Voronoi Diagram with Exactly 4 Half-Line Edges');
xlabel('X');
ylabel('Y');
grid;
axis equal;
hold off;
