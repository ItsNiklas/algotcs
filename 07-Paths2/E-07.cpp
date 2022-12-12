#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

// Struct to represent a city with its coordinates.
struct City {
    int x, y;
};

// Struct to represent an edge between two cities.
struct Edge {
    int u, v;
    double w;
};

// Union-find data structure to keep track of connected components
// and check whether two cities are already connected.
class UnionFind {
    std::vector<int> parent, rank;

  public:
    explicit UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    int find(int u) {
        if (parent[u] != u)
            parent[u] = find(parent[u]);
        return parent[u];
    }

    void merge(int u, int v) {
        int p = find(u);
        int q = find(v);
        if (p == q)
            return;
        if (rank[p] < rank[q])
            parent[p] = q;
        else if (rank[q] < rank[p])
            parent[q] = p;
        else {
            parent[p] = q;
            rank[q]++;
        }
    }

    bool connected(int u, int v) { return find(u) == find(v); }
};

int main() {
    int n;
    std::cin >> n;

    std::vector<City> cities(n);
    for (int i = 0; i < n; i++)
        std::cin >> cities[i].x >> cities[i].y;

    std::vector<Edge> edges;

    // Calculate the distances between all pairs of cities
    // and add them to the list of edges.
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double dx = cities[i].x - cities[j].x;
            double dy = cities[i].y - cities[j].y;
            double distance = sqrt(dx * dx + dy * dy);
            Edge e = {i, j, distance};
            edges.push_back(e);
        }
    }

    // Sort the edges in ascending order of their weight.
    sort(edges.begin(), edges.end(),
         [](const Edge &a, const Edge &b) { return a.w < b.w; });

    UnionFind uf(n);
    double min_total_length = 0;

    // For each edge, check if the cities it connects are already connected.
    // If they are not, add the edge to the minimum spanning tree and
    // update the total length of the roads.
    for (const Edge &e : edges) {
        if (!uf.connected(e.u, e.v)) {
            uf.merge(e.u, e.v);
            min_total_length += e.w;
        }
    }

    // Print the minimum total length of the roads.
    printf("%.7f\n", min_total_length);

    return 0;
}
