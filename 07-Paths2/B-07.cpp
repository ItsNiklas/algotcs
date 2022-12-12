#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

int find(int node, std::vector<int> &parents) {
    // Function to find the parent of a given node.
    // If the given node is the parent of itself, return it.
    if (parents[node] == node) {
        return node;
    }
    // Otherwise, recursively find the parent of the given node.
    parents[node] = find(parents[node], parents);
    return parents[node];
}

bool merge(int node1, int node2, std::vector<int> &parents, std::vector<int> &ranks) {
    // Function to merge two nodes.
    // Find the parent of each node.
    int parent1 = find(node1, parents);
    int parent2 = find(node2, parents);

    // If the nodes have the same parent, they are already in the same set.
    if (parent1 == parent2) {
        return false;
    }
    // Otherwise, set the parent of the second node as the parent of the first node.
    if (ranks[parent1] > ranks[parent2]) {
        parents[parent2] = parent1;
    } else {
        parents[parent1] = parent2;
        if (ranks[parent1] == ranks[parent2]) {
            ranks[parent2] += 1;
        }
    }
    return true;
}

int main() {
    // Store the input in variables n, m, p1 and p2.
    int n, m, p1, p2;
    std::cin >> n >> m >> p1 >> p2;

    // Initialize the total amount of honey to 0.
    int total_honey = 0;

    // Create a list of edges, where each edge is a tuple containing the coordinates
    // of the two states and the weight of the edge.
    std::vector<std::tuple<int, int, int>> edges;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // Calculate the coordinates of the current state.
            int x1 = i, y1 = j;

            // Calculate the amount of honey required to connect the current state
            // to each of its neighbors.
            std::vector<std::pair<int, int>> neighbors = {
                {i - 1, j - 1}, {i - 1, j}, {i, j - 1},
                {i, j + 1},     {i + 1, j}, {i + 1, j + 1}};
            for (auto gag : neighbors) {
                auto x2 = std::get<0>(gag);
                auto y2 = std::get<1>(gag);
                // Check if the neighbor is a valid state in the honeycomb.
                if (1 <= x2 && x2 <= n && 1 <= y2 && y2 <= m) {
                    // Check if the neighbor has a smaller row and column index than
                    // the current state, to avoid adding the same edge multiple times.
                    if (x2 < x1 || (x2 == x1 && y2 < y1)) {
                        // Add the amount of honey required to connect the two states
                        // to the list of edges.
                        int weight = (x1 * x2 + p1 * y1 * y2) % p2;
                        // Index = x * width + y
                        int idx = (x1 - 1) * m + y1 - 1;
                        int idy = (x2 - 1) * m + y2 - 1;
                        edges.emplace_back(idx, idy, weight);
                    }
                }
            }
        }
    }

    // Sort the list of edges in ascending order of weight.
    sort(edges.begin(), edges.end(), [](const auto &e1, const auto &e2) {
        return std::get<2>(e1) < std::get<2>(e2);
    });

    // Parents array to store the parent of each node.
    // Initially, each node is a parent of itself.
    std::vector<int> parents(n * m);
    for (int i = 0; i < n * m; i++) {
        parents[i] = i;
    }

    // Rank array to store the rank of each node.
    // Initially, each node has rank 0.
    std::vector<int> ranks(n * m, 0);

    // Kruskal
    for (auto e : edges) {
        int u, v, c;
        std::tie(u, v, c) = e;
        if (merge(v, u, parents, ranks)) {
            total_honey += c;
        }
    }

    // Output the total amount of honey
    std::cout << total_honey << std::endl;

    return 0;
}
