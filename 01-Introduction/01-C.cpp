#include <iostream>

int main() {
    // Read integers from stdin.
    int buoys, flood, height;
    std::cin >> buoys >> flood;

    // Loop over buoys.
    for (int i = 1; i <= buoys; i++) {
        std::cin >> height;
        if (height < flood) {
             std::cout << i << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}