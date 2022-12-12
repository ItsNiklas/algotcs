#include <iostream>      // for cin, cout
#include <map>           // for queries
#include <set>           // children
#include <unordered_map> // faster array
#include <vector>        // for vector

struct Edge {
    int from;
    int to;
};

int num_vertices, num_edges, num_queries;
std::unordered_map<int, int> parent;
std::unordered_map<int, int> ranks;
std::unordered_map<int, std::set<int>> children;
std::map<int, std::vector<std::pair<int, int>>> queries; // From : [To, Answer_idx]
std::unordered_map<int, int> answers;
std::vector<Edge> edgelist;

int find(int vertex) {
    // Find function to determine the representative element of a set.
    int root = vertex;
    while (root != parent[root]) {
        root = parent[root];
    }

    // Compress the path from the vertex to the root by pointing each vertex
    // directly to the root. This optimizes the time it takes to find the root
    // of the set in the future.
    while (vertex != root) {
        int next = parent[vertex];
        parent[vertex] = root;
        vertex = next;
    }

    return root;
}

bool merge(int vertex1, int vertex2, int time) {
    // Merge function to merge two sets.
    // Find the roots of the sets that the vertices belong to.
    int root1 = find(vertex1);
    int root2 = find(vertex2);

    // If the vertices are already in the same set, return.
    if (root1 == root2)
        return false;

    // ANSWER QUERIES by iterating over the smaller set (!).
    if (children[root1].size() > children[root2].size())
        std::swap(root1, root2);

    for (int from : children[root1]) {
        for (std::pair<int, int> entry : queries[from]) {
            int to = entry.first;
            int idx = entry.second;
            const bool is_in = children[root2].find(to) != children[root2].end();
            // Lock answer if we are actually merging a new connection.
            if (is_in && answers[idx] == 0)
                answers[idx] = time;
        }
    }

    // Link by rank:
    // Merge the smaller set into the larger set by attaching the root of the
    // smaller set to the root of the larger set.
    if (ranks[root1] == ranks[root2])
        ranks[root1]++;
    if (ranks[root1] < ranks[root2])
        std::swap(root1, root2);
    parent[root1] = root2;

    // Merge all children from smaller set into the larger one.
    children[root2].insert(children[root1].begin(), children[root1].end());

    return true;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // Read input.
    std::cin >> num_vertices >> num_edges >> num_queries;

    // Initialize the disjoint set with n singleton sets, one for each vertex.
    for (int i = 1; i <= num_vertices; i++) {
        parent[i] = i;
        ranks[i] = 0;
        children[i].insert(i);
    }

    // For each edge, read the vertices.
    for (int i = 0; i < num_edges; i++) {
        int vertex1, vertex2;
        std::cin >> vertex1 >> vertex2;
        edgelist.push_back({vertex1, vertex2});
    }

    // For each query, read the vertices to be checked for the same set.
    for (int i = 0; i < num_queries; i++) {
        int vertex1, vertex2;
        std::cin >> vertex1 >> vertex2;

        queries[vertex1].emplace_back(vertex2, i);
        queries[vertex2].emplace_back(vertex1, i);
    }

    // Run simulation.
    for (int time = 1; time <= num_edges; ++time) {
        Edge e = edgelist[time - 1];
        merge(e.from, e.to, time);
    }

    // Print.
    for (int i = 0; i < num_queries; ++i) {
        std::cout << answers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}