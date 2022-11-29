#include <vector>
#include <iostream>

const int INF = 1e9, MAXN = 2001;
struct edge {
	int v, u, xp;
};


int main(){
    int N, M, b, a, v;
    std::cin >> N >> M;
    
    std::vector<edge> edgelist;
    int dist[MAXN];

    for (int i = 0; i < M; i++){
        std::cin >> b >> a >> v;
        // Read edgelist, inverting the knowledge.
        edgelist.push_back({b, a, -v});
    }

    // Bellman-Ford.
    // Used to find negative cycles.
    std::fill(dist, dist + N + 1, INF);
    dist[1] = 0;

    for (int k = 1; k <= 2 * N - 1; k++){
        for (edge e : edgelist) {
            if (dist[e.v] == INF) continue;
            if (dist[e.v] + e.xp < dist[e.u]) {
                if (k > N - 1)
                    dist[e.u] = -INF;
                else
                    dist[e.u] = dist[e.v] + e.xp;
            }
        }
    }

    // Print result.
    // Check for a infinite circle occuring.
    int res = -dist[N];

    if (res == INF)
        std::cout << ":)" << std::endl;
    else if (res == -INF)
        std::cout << ":(" << std::endl;
    else
        std::cout << res << std::endl;
}