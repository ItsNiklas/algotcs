#include <iostream>
#include <map>

// Abusing map being implemented as a balanced binary search tree.
// Complexity: O(log n).
std::map<int, int> S;

void add(int i) {
    S[i] = i;
}

int next(int i) {
    // And abusing the upper_bound function.
    auto it = S.upper_bound(i - 1);
    if (it == S.end()) {
        return -1;
    } else {
        return it->first;
    }
}

int main() {
    int n, i, y;
    char q;
    bool mod = false;

    std::cin >> n;
    while (std::cin >> q >> i) {
        if (q == '+') {
            add(mod ? (i + y) % 1000000000 : i);
            mod = false;
        } else {
            std::cout << (y = next(i)) << std::endl;
            mod = true;
        }
    }

    return 0;
}