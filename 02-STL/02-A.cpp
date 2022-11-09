#include <iostream>
#include <string>

int main() {
    std::string a, b;

    std::getline(std::cin, a);
    std::getline(std::cin, b);
    
    // Print to stdout.
    std::cout << (a.length() >= b.length() ? "go" : "no") << std::endl;
    return 0;
}