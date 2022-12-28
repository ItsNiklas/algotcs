#include <iostream>
#include <unordered_set>
#include <vector>

const int MAX_N = 10005;

// Mex (Minimal Exclusion) function.
int mex(std::unordered_set<int> values) {
    int i = 0;
    while (values.find(i) != values.end())
        i++;
    return i;
}

int main() {
    int T;
    std::cin >> T;

    std::vector<int> g(MAX_N);
    std::vector<int> kl(MAX_N);
    
    // Fill Result Vector bottom-up, DP-like.
    for (int x = 0; x < MAX_N; x++){
        int k = 0, z = 0;
        std::unordered_set<int> s;

        // All possible divisions.
        for (int y = 1; y < x/2 + 1; y++) {
            // The two halves should be of different sizes.
            if (y == (z = x - y)) continue;

            s.emplace(g[y] ^ g[z]); // Fill set.
            if (!(g[y] ^ g[z])) k++; // Count winning move.
        }
        
        g[x] = mex(s);
        kl[x] = k;
    }
    
    // Answer queries.
    while (T--) {
        int n;
        std::cin >> n;
        std::cout << kl[n] << std::endl;
    }

    return 0;
    
}
