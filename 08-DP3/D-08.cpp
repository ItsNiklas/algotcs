#include <iostream>
#include <vector>

const int MAXN = 100005;

int n, gain[MAXN];
std::vector<int> adj[MAXN];
int dp[MAXN], mx = -1;

void dfs(int u, int p) {
    dp[u] = gain[u];
    for (int v : adj[u]) {
        if (v == p)
            continue;
        dfs(v, u);
        dp[u] += std::max(0, dp[v]);
    }
    mx = std::max(mx, dp[u]);
}

int main() {
    std::cin >> n;

    for (int i = 1; i <= n; i++)
        std::cin >> gain[i];

    for (int i = 1; i < n; i++) {
        int a, b;
        std::cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(1, -1);
    std::cout << mx << std::endl;

    return 0;
}