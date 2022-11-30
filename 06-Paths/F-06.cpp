#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <limits>

const int INF = std::numeric_limits<int>::max(), MAXN = 251, MAXM = 20001;
const double INFD = std::numeric_limits<double>::infinity();
struct edge {
	int u, cost;
};
struct score {
    double t;
    int s;
};


int main(){
    std::vector<edge> edges[MAXN];
    int N, M, F, c, v, u, l;
    double vel;

    // Read all inputs.
    std::cin >> N >> M >> F;
    std::cin >> c >> vel;

    int shelter_idx[F];
    for (auto &idx : shelter_idx)
        std::cin >> idx;

    // Establish Adjacency list.
    for (int i = 0; i < M; i++){
        std::cin >> v >> u >> l;
        edges[v].push_back({u, l});
        edges[u].push_back({v, l});
    }

    // SPFA.
    // Vector stores tuples of possible times and steps at i.
    // Time and steps need to be tied together.
    int used[MAXN];
    std::vector<score> time[MAXN];
    
    for (auto &v : time) v.push_back({INFD, INF});
    time[c].push_back({0.0, 0});

    std::queue<int> q; q.push(c);

    while (!q.empty()) {
        int vertex = q.front(); q.pop();
        used[vertex] = 0;

        // Iterate over all possible states possible at vertex.
        for (auto state : time[vertex]) {
            for (edge e : edges[vertex]) {
            
                // Time needed to pass edge.
                double cost = e.cost / (std::pow(0.9, state.s) * vel);

                // Minimal cost and steps for node.
                // Inefficiently iterating over tuple vector
                // with custom comparison.
                auto min_cost_next = std::min_element(time[e.u].begin(), time[e.u].end(),
                                         [](auto& lhs, auto& rhs) { return lhs.t < rhs.t; }) -> t;
                auto min_steps_next = std::min_element(time[e.u].begin(), time[e.u].end(),
                                          [](auto& lhs, auto& rhs) { return lhs.s < rhs.s; }) -> s;

                // In some way the new state is better.
                if (cost + state.t < min_cost_next || state.s + 1 < min_steps_next) {

                    // Append to possible states at node next (e.u).
                    // Optimization: Clear or replace so maximum number of elements is <= 2.
                    time[e.u].push_back({state.t + cost, state.s + 1});
                    
                    if (!used[e.u]) {
                        q.push(e.u);
                        used[e.u] = 1;
                    }
                }
            }
        }
    }

    // Find minimal distance inside all shelter states.
    double min = INFD;
    for (int idx : shelter_idx) {
        double new_min = std::min_element(time[idx].begin(), time[idx].end(),
                             [](auto& lhs, auto& rhs) { return lhs.t < rhs.t; }) -> t;
        min = std::min(min, new_min);
    }

    // Print result.
    std::cout.precision(8);
    std::cout << std::fixed << min << std::endl;

    return 0;
}