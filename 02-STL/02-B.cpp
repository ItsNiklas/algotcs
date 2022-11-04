#include <iostream>
#include <string>
#include <algorithm>

int main() {
    // Read until \0 or EOF. Unsafe but simple.
    std::string in;
    std::getline(std::cin, in, '\0');

    // Reverse. Keep a \n at the end.
    std::reverse(in.begin(), in.end());
    
    // Print to stdout.
    std::cout << in;
    return 0;
}