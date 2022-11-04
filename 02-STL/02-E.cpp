#include <iostream>
#include <queue>


int main() {
    // Initialize cookie holding area.
    // Implemented as a double priority queue.
    // Solution via sreeprasad, 2018: https://sreeprasad.medium.com/98a3f56b8142
    std::priority_queue<int, std::vector<int>, std::greater<>> qmin;
    std::priority_queue<int, std::vector<int>, std::less<>> qmax;
    
    std::string input;
    int val;
    
    while (std::cin >> input) {
        if (input == "#") {
            // Return Median position. This is always qmin.top() by queue design.
            std::cout << qmin.top() << std::endl, qmin.pop();

            // Rebalance.
            if (qmin.size() != qmax.size())
                qmin.push(qmax.top()), qmax.pop();
            
        } else {
            // Insert cookie into correct queue.
            val = std::stol(input);
            if (qmin.size() == 0) 
                qmin.push(val);
            else 
                val > qmin.top() ? qmin.push(val) : qmax.push(val);

            // Rebalance.
            if (qmin.size() > qmax.size() + 1) 
                qmax.push(qmin.top()), qmin.pop();
            else if (qmin.size() < qmax.size()) 
                qmin.push(qmax.top()), qmax.pop();
        }
    }
    
    return 0;
}