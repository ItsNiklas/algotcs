#include <iostream>
#include <algorithm>
#include <vector>


int main() {
    // Read from stdin.
    // Set up variables.
    int T, tmp; std::cin >> T;
    int input[T];
    for(int& t : input) std::cin >> t;
    int max_m = *std::max_element(input, input + T) + 1;

    // Find minimal required pyramid sizes
    std::vector<int> pyramids = {1};
    for(int n = 1; pyramids[n - 1] < max_m; n++)
        pyramids.push_back(n*(n+1)*(n+2)/6);
    pyramids.pop_back();

    // Create cache.
    int table[max_m];
    std::fill_n(table, max_m, max_m);
    table[0] = 0;

    // Fill cache.
    // This is identical to a coin change problem at this point.
    for(int m = 0; m < max_m; ++m){
        for(int p : pyramids){
            if (p <= m) {
                tmp = table[m - p];
                if (tmp != max_m && tmp + 1 < table[m]) table[m] = tmp + 1;
            } else break;
        }        
    }

    // Print respective results.
    for (int t : input) std::cout << table[t] << std::endl;
        
    return 0;
}