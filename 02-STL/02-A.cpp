#include <iostream>

int main() {
    int d = 0;
    char c;

    // Calculating difference of a's.
    // Switches to doctor after 'h'.
    while (std::cin >> c) {
        d += c == 'a';
        if (c == 'h') d *= -1;
    }
    
    // Print to stdout.
    std::cout << (d >= 0 ? "go" : "no") << std::endl;
    return 0;
}