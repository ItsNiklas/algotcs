#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    int seq[n];

    // Read sequence.
    for (auto& i : seq)
        std::cin >> i;

    // Sort in descending order.
    std::sort(seq, seq + n, std::greater<int>());
    
    // Print to stdout.
    for (const auto& i : seq)
        std::cout << i << " ";
    std::cout << std::endl;
    return 0;
}