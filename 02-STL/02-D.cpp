#include <iostream>
#include <map>

int main() {
    // Initialize.
    int n, m, k;
    std::cin >> n, std::cin >> m;
    
    // Collect existing hashes and store in a map (tree).
    std::map<int, int> hashes;
    for (int i = 1; i <= n; i++)
          std::cin >> k, hashes[k] = i;
    
    // Last occurence is now automatically stored in map.
    // Print found, 0 otherwise.
    while (std::cin >> m) {
        std::map<int, int>::iterator result = hashes.find(m);
        std::cout << (result != hashes.end() ? result->second : 0) << std::endl;
    }
    
    return 0;
}