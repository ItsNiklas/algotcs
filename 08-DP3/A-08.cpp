#include <cstring>
#include <iostream>
#include <vector>

const int MAXN = 1e5 + 5;

int n, m;
int dp[MAXN];

std::vector<int> adj[MAXN];

int dfs(int u) {
    if (dp[u] != -1)
        return dp[u];
    dp[u] = 0;
    for (int v : adj[u]) {
        dp[u] = std::max(dp[u], dfs(v) + 1);
    }
    return dp[u];
}

int main() {
    std::cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        std::cin >> a >> b;
        adj[a].push_back(b);
    }

    std::memset(dp, -1, sizeof(dp));
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        ans = std::max(ans, dfs(i));
    }
    std::cout << ans << std::endl;
    return 0;
}
