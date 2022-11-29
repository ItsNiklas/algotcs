#include <vector>
#include <iostream>
#include <cmath>
#include <limits>

const int INF = std::numeric_limits<int>::max(), MAXM = 500000, MAXN = 501;
const double INFD = std::numeric_limits<double>::max();

struct edge {
	int u, v;
    double d;
};
struct obj {
    int x, y, z;
};


double dist(obj o1, obj o2){
    return std::sqrt(std::pow((o2.x-o1.x), 2) + std::pow((o2.y-o1.y), 2) + std::pow((o2.z-o1.z), 2));
}


int main(){
    int N, M;
    std::cin >> N >> M;
    
    int V = N + M;
    
    std::vector<edge> edgelist;
    std::vector<obj> objects = {{0,0,0}};

    // Read stars & wormholes.
    for (int i = 1; i <= V; i++){
        int x, y, z;
        std::cin >> x >> y >> z;
        objects.push_back({x,y,z});

        // Establish edges to all previous objects.
        for (int k = 1; k < i; k++) {
            // Optimization: Possible to skip adjacent wormhole connections here.
            double di = dist(objects[i], objects[k]);
            edgelist.push_back({i, k, di});
            edgelist.push_back({k, i, di});
        }
    }

    // Establish shortcuts through wormholes.
    for (int i = N + 1; i < V; i += 2){    
        edgelist.push_back({i, i+1, 0.0});
        edgelist.push_back({i+1, i, 0.0});
    }

    // Floyd-Warshall.
    // Could be optimized for bidirectional edges.
    double d[MAXN][MAXN];

    std::fill_n(&d[0][0], MAXN*MAXN, INFD);

    for (auto e : edgelist)
        d[e.v][e.u] = e.d;

    for (int v = 1; v <= V; v++)
        d[v][v] = 0;

    for (int k = 1; k <= V; k++)
        for (int i = 1; i <= V; i++)
            for (int j = 1; j <= V; j++)
                if (d[i][k] != INFD && d[k][j] != INFD)
                    d[i][j] = std::min(d[i][j], d[i][k] + d[k][j]);


    // Print resulting matrix.
    std::cout.precision(5);
    for (int i = 1; i <= N; ++i){
        for (int k = 1; k <= N; ++k) std::cout << std::fixed << d[i][k] << " ";
        std::cout << std::endl;
    }
}