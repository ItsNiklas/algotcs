#include <iostream>

int main() {
    // Read integers from stdin.
    int cases, customers;
    std::cin >> cases;

    // Loop over cases.
    for (int i = 0; i < cases; i++) {
        std::cin >> customers;
        // Store numbers in array.
        int queue[customers];
        for (int k = 0; k < customers; k++) {
            std::cin >> queue[k];
        }
        // Print in reverse order.
        for (int k = customers - 1; k >= 0; k--) {
            std::cout << queue[k] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}