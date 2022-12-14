// This program uses Dijkstra's algorithm to find the minimum authentication level
// needed to reach a room adjacent to the command center.

#include <iostream>
#include <queue>
#include <vector>

const int MAXN = 1e5 + 10; // Maximum number of rooms, halls, and hallways
const int INF = 1e9;       // Maximum authentication level

// Edge represents a door connecting two rooms with a given authentication level
struct Edge {
    int to, weight;

    Edge(int to, int weight) : to(to), weight(weight) {}
};

int n, m, s, t;
// Number of rooms, number of doors, starting room, and command center room
std::vector<Edge> edges[MAXN]; // Adjacency list representing the rooms and doors
int d[MAXN];    // Array to store minimum authentication levels for each room
bool vis[MAXN]; // Array to keep track of visited rooms in Dijkstra's algorithm

void dijkstra() {
    std::priority_queue<std::pair<int, int>> q; // Store potential next steps
    q.emplace(0, s);                            // Add starting room to queue
    d[s] = 0; // Set authentication level for starting room to 0

    while (!q.empty()) {
        int u = q.top().second; // Get next room with minimum authentication level
        q.pop();

        // Skip room if it has already been visited
        if (vis[u])
            continue;
        vis[u] = true;

        // Iterate through doors connected to current room
        for (unsigned int i = 0; i < edges[u].size(); i++) {
            int v = edges[u][i].to;     // Get destination room for current door
            int w = edges[u][i].weight; // Get authentication level for current door
            if (d[v] > std::max(d[u], w)) {
                // Update destination room's authentication level if necessary
                d[v] = std::max(d[u], w);
                q.emplace(-d[v], v); // Add destination room to priority queue
            }
        }
    }
}

int main() {
    std::cin >> n >> m >> s >> t; // Read in number of rooms, number of doors, starting
                                  // room, and command center room

    for (int i = 0; i < m; i++) { // Read in information for each door
        int u, v, w;
        std::cin >> u >> v >> w;
        edges[u].emplace_back(v, w); // Add door to adjacency list for room u
        // Add door to adjacency list for room v (since doors are bidirectional)
        edges[v].emplace_back(u, w);
    }

    // Initialize minimum authentication levels for each room to INF
    for (int i = 1; i <= n; i++)
        d[i] = INF;

    dijkstra();

    int ans = INF;
    // Initialize minimum required authentication level to INF
    // Iterate through doors connected to command center
    for (auto &i : edges[t]) {
        int v = i.to; // Get destination room for current door
        ans = std::min(ans, d[v]);
    }
    std::cout << ans << std::endl; // Output minimum required authentication level
    return 0;
}