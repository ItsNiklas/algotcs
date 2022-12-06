#include <iostream> // for cin, cout
#include <vector> // for vector
#include <unordered_map>
#include <algorithm> // for reverse

const int MAX_VERTICES = 5 * 1e4 + 5; // maximum number of vertices

int num_vertices, num_edges, num_queries; // number of vertices, edges and queries
std::unordered_map<int, int> parent;
std::unordered_map<int, int> ranks;

struct Query {
    int type;
    int from;
    int to;
};

// find function to determine the representative element of a set
int find(int vertex) {
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

// merge function to merge two sets
bool merge(int vertex1, int vertex2) {
    // find the roots of the sets that the vertices belong to.
    int root1 = find(vertex1);
    int root2 = find(vertex2);

    // If the vertices are already in the same set, return.
    if (root1 == root2) return false;

    // Merge the smaller set into the larger set by attaching the root of the
    // smaller set to the root of the larger set.
    if (ranks[root1] < ranks[root2]) {
        parent[root1] = root2;
    } else if (ranks[root1] > ranks[root2]) {
        parent[root2] = root1;
    } else {
        parent[root1] = root2;
        ++ranks[root2];
    }
    return true;
}

int main() {
    // read input
    std::cin >> num_vertices >> num_edges >> num_queries;

    // initialize the disjoint set with n singleton sets, one for each vertex
    for (int i = 1; i <= num_vertices; i++) {
        parent[i] = i;
        ranks[i] = 0;
    }

    // for each edge, read the vertices (And void because we don't need this information)
    for (int i = 0; i < num_edges; i++) {
        int vertex1, vertex2;
        std::cin >> vertex1 >> vertex2;
    }

    // for each query, read the vertices and type of query
    std::vector<Query> queries;
    for (int i = 0; i < num_queries; i++) {
        std::string type;
        int vertex1, vertex2;
        std::cin >> type >> vertex1 >> vertex2;
        queries.push_back({(type == "ask") ? 1 : 0, vertex1, vertex2});
    }

    // Iterate over queries, reversed.
    std::vector<std::string> output;
    for (auto it = queries.rbegin(); it != queries.rend(); ++it) {
        auto q = *it;
        if (q.type == 0) { //Instead of cutting, we merge, because it is reversed.
            merge(q.from, q.to);
        } else { // Actually find out if they are in the same subgraph.
            output.emplace_back((find(q.from) == find(q.to) ? "YES" : "NO"));
        }
    }

    //reverse the output again.
    std::reverse(output.begin(), output.end());
    for (const auto &s: output) {
        std::cout << s << std::endl;
    }

    return 0;
}

