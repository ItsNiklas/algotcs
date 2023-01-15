#include <iostream>
#include <set>

// Set blocksize to √N.
// Create array to store all values & set for block lookups.
const int BLSIZE = 513, MAXN = 1e5;
long a[MAXN + 1];
std::set<long> block[MAXN / BLSIZE + 1];

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, m, b, Q, l, r, d;
    std::cin >> N >> m >> b;

    // Read and precalculate residuals.
    for (int i = 1; i <= N; ++i) {
        std::cin >> d;
        long v = std::abs(d - (m * i + b));

        a[i] = v;
        block[i / BLSIZE].insert(v);
    }

    // Answer queries
    std::cin >> Q;
    while (std::cin >> l >> r >> d) {
        // Get block indices.
        int l_bl = l / BLSIZE, r_bl = r / BLSIZE;
        long res = UINT64_MAX;

        // l & r are in the same block
        if (l_bl == r_bl) {
            for (int i = l; i <= r; i++) {
                if (a[i] <= d)
                    continue;
                res = std::min(res, a[i]);
            }
        } else {
            // Left partial block
            for (int i = l; i < (l_bl + 1) * BLSIZE; i++) {
                if (a[i] <= d)
                    continue;
                res = std::min(res, a[i]);
            }
            // Fully contained blocks, look at sets and abuse set::upper_bound,
            // as implementation is based on a Rb tree.
            for (int i_bl = l_bl + 1; i_bl < r_bl; i_bl++) {
                res = std::min(res, *block[i_bl].upper_bound(d));
            }
            // Right partial block
            for (long i = r_bl * BLSIZE; i <= r; i++) {
                if (a[i] <= d)
                    continue;
                res = std::min(res, a[i]);
            }
        }

        std::cout << (res == INT64_MAX ? -1 : res) << std::endl;
    }

    return 0;
}