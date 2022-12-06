#include<bits/stdc++.h>

// n is the number of junctions
// m is the number of roads
int n, m;

// fa[i] is the parent of junction i in the disjoint set
int fa[100005];

// val[i] is 1 if road i is non-horrible, 0 otherwise
int val[100005];

// Find the representative of the set containing x
int find(int x) {
    // If x is the parent of itself, x is the representative
    // of its set.
    if (fa[x] == x)
        return x;

    // Otherwise, we recursively call find on the parent
    // of x and assign the result to the parent of x.
    // This is done to perform path compression, which
    // helps to reduce the time complexity of subsequent
    // calls to find on the same set.
    return fa[x] = find(fa[x]);
}

int main() {
    std::cin >> n >> m;

    // Initialize the disjoint set
    for (int i = 1; i <= n; i++) fa[i] = i;

    // For each road, check if it connects two different
    // connected components. If it does, merge the two
    // connected components. Otherwise, the road must
    // be part of a cycle, and we mark it as "horrible".
    for (int i = 1; i <= m; i++) {
        int u, v;
        std::cin >> u >> v;

        // Find the representatives of the sets containing
        // u and v.
        u = find(u), v = find(v);

        // If the representatives are different, the road
        // connects two different connected components,
        // so we merge them by assigning the representative
        // of one of the sets as the parent of the other.
        if (u != v) {
            fa[u] = v;

            // Mark the road as non-horrible
            val[i] = 1;
        }
    }

    // Count the number of non-horrible roads
    int num_non_horrible_roads = 0;
    for (int i = 1; i <= m; i++)
        if (val[i]) num_non_horrible_roads++;

    // Print the number of non-horrible roads
    std::cout << num_non_horrible_roads << std::endl;

    // Print the indices of the non-horrible roads
    for (int i = 1; i <= m; i++)
        if (val[i]) std::cout << i << " ";
    std::cout << std::endl;
    return 0;
}
