#include <iostream>

int main() {
    // Read integers from stdin.
    int cases;
    unsigned long long int n; // Need 10^18 digits.
    std::cin >> cases;

    // Loop over cases.
    for (int i = 0; i < cases; i++) {
        std::cin >> n;
        // Described behaviour is equivalent to quadratic growth.
        std::cout << (n+1)*(n+1) << std::endl;
    }
    return 0;
}