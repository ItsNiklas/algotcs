#include <vector>
#include <set>
#include <iostream>
#include <limits>

const int INF = std::numeric_limits<int>::max(), MAXN = 50001;
const double INFD = std::numeric_limits<double>::max();
struct edge {
	int v;
    double t;
    int l;
};


int main(){
    int N, M, Q, b, e, v, l;
    std::cin >> N >> M;
        
    std::vector<edge> edges[MAXN];
    int dis[MAXN];
    double tim[MAXN];

    // Create Adjacency list.
    // Time is calculated and used.
    for (int i = 0; i < M; i++){
        std::cin >> b >> e >> v >> l;
        double t = l / (double) v;
        edges[b].push_back({e, t, l});
        edges[e].push_back({b, t, l});
    }

    int root = 1;

    // Dijkstra 1.
    // Optimized and for minimal distance.
    std::fill(dis, dis+N+1, INF);
    dis[root] = 0;
    std::set<std::pair<int,int>> dst;
    dst.insert({dis[root], root});
    while (!dst.empty()) {
        int vertex = dst.begin()->second;
        dst.erase(dst.begin());
        for (edge e : edges[vertex]) {
            if (dis[vertex] + e.l < dis[e.v]) {
                dst.erase({dis[e.v], e.v});
                dis[e.v] = dis[vertex] + e.l;
                dst.insert({dis[e.v], e.v});
            }
        }
    }

    // Dijkstra 2
    // Optimized and for minimal time.
    std::fill(tim, tim+N+1, INFD);
    tim[root] = 0.0;
    std::set<std::pair<double,int>> dsf;
    dsf.insert({tim[root], root});
    while (!dsf.empty()) {
        int vertex = dsf.begin()->second;
        dsf.erase(dsf.begin());
        for (edge e : edges[vertex]) {
            if (tim[vertex] + e.t < tim[e.v]) {
                dsf.erase({tim[e.v], e.v});
                tim[e.v] = tim[vertex] + e.t;
                dsf.insert({tim[e.v], e.v});
            }
        }
    }

    // Answer queries.
    std::cin >> Q;
    std::cout.precision(8);

    for (int i = 0; i < Q; i++){
        int j; char c;
        std::cin >> j >> c;
        
        if (c == 'f') {
            if (tim[j] == INFD) std::cout << "IMPOSSIBLE" << std::endl;
            else std::cout << std::fixed << tim[j] << " h" << std::endl;
        } else {
            if (dis[j] == INF) std::cout << "IMPOSSIBLE" << std::endl;
            else std::cout << dis[j] << " km" << std::endl;
        }
    }
    
    return 0;
}