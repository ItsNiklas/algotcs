#include <vector>
#include <deque>
#include <iostream>

const int MAXN = 1000001;
struct edge {
	int u, cost;
};


int main(){
    int V, E, u, v;
    char l;
    std::cin >> V >> E;

    std::vector<edge> edges[MAXN];

    // Create directed Adjacency list.
    for (int i = 0; i < E; i++) {
        std::cin >> u >> v >> l;
        edge e = {v, l == 'l' ? 1 : 0};
        edges[u].emplace_back(e);
    }

    // BFS 0-1.
    // Implemented with a double-ended queue.
    std::deque<int> q;
    int d[MAXN];
    std::fill(d, d + MAXN, MAXN);

	d[1] = 0;
	q.push_back(1);
    
	while(!q.empty()) {
		int vertex = q.front(); q.pop_front();

        if (vertex == V){
            // Exit found.
            // Minimal distance is calculated at this point,
            // because of BFS.
            std::cout << d[V] << std::endl;
            return 0;
        }
        
		for(edge next : edges[vertex]){
			if(d[vertex] + next.cost < d[next.u]) {
				d[next.u] = d[vertex] + next.cost;

                // Simulate a 0/1 Priority Queue.
				if(!next.cost) q.push_front(next.u);
				else q.push_back(next.u);
			}
        }
	}

    // Not reachable.
    std::cout << -1 << std::endl;
    
    return 0;
}