% Define the fixed points
points = [-1, 6;   % A
          -1, -1;  % B
           4, 7;   % C
           6, 7;   % D
           1, -1;  % E
          -5, 3;   % F
          -2, 3];  % P

% Define the parameterized point Q
lambda_values = linspace(-10, 10, 1000); % Range of lambda for evaluation
min_mst_length = Inf; % Initialize the minimum MST length
optimal_lambda = NaN; % To store the optimal lambda

for lambda = lambda_values
    % Compute Q based on lambda
    Q = [2 - lambda, 3];
    
    % Add Q to the points list
    all_points = [points; Q];
    
    % Compute the distances between all pairs of points
    n = size(all_points, 1);
    dist_matrix = zeros(n, n);
    for i = 1:n
        for j = i+1:n
            dist_matrix(i, j) = norm(all_points(i, :) - all_points(j, :));
            dist_matrix(j, i) = dist_matrix(i, j); % Symmetric matrix
        end
    end
    
    % Compute the Minimum Spanning Tree (MST) using Prim's algorithm
    G = graph(dist_matrix, 'upper');
    T = minspantree(G);
    mst_length = sum(T.Edges.Weight);
    
    % Update the minimum MST length and optimal lambda
    if mst_length < min_mst_length
        min_mst_length = mst_length;
        optimal_lambda = lambda;
    end
end

% Display the result
fprintf('Optimal lambda: %.4f\n', optimal_lambda);
fprintf('Minimum MST length: %.4f\n', min_mst_length);

% Plot MST and points for the optimal lambda
optimal_Q = [2 - optimal_lambda, 3];
all_points_optimal = [points; optimal_Q];

% Recompute distances for the optimal lambda
n = size(all_points_optimal, 1);
dist_matrix_optimal = zeros(n, n);
for i = 1:n
    for j = i+1:n
        dist_matrix_optimal(i, j) = norm(all_points_optimal(i, :) - all_points_optimal(j, :));
        dist_matrix_optimal(j, i) = dist_matrix_optimal(i, j); % Symmetric matrix
    end
end

% Generate graph for MST
G_optimal = graph(dist_matrix_optimal, 'upper');
T_optimal = minspantree(G_optimal);

% Plot the MST and points
figure;
hold on;
plot(T_optimal, 'XData', all_points_optimal(:, 1), 'YData', all_points_optimal(:, 2), 'LineWidth', 2);
scatter(all_points_optimal(:, 1), all_points_optimal(:, 2), 50, 'r', 'filled'); % Plot points
text(all_points_optimal(:, 1), all_points_optimal(:, 2), ...
     {'A', 'B', 'C', 'D', 'E', 'F', 'P', 'Q'}, ...
     'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');

% Add labels and title
title(sprintf('MST for Optimal Lambda (%.4f)', optimal_lambda));
xlabel('X');
ylabel('Y');
axis equal;
grid on;
hold off;
