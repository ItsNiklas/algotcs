#include <iostream>

// Explanation in B-09.py.

int main() {
    long n, k;
    std::cin >> k;
    while (std::cin >> n >> k) {
        k = k > n ? n : k; // Fix overflow if k > n
        long o = (n - k) % (k + 2) - 2;
        std::cout << (o < 0 ? k : o) << std::endl;
    }

    return 0;
}