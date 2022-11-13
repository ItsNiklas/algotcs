from functools import lru_cache
from typing import Union


def main() -> None:
    # Read from stdin.
    input = list(map(int, [x.split() for x in open(0)][1]))

    # Memoization à la Python.
    # Using the Least Recently Used Cache decorator.
    @lru_cache(None)
    def dp(i: int) -> Union[float, int]:
        if i < 0: return float('-inf') # Out of bounds
        if i == 0: return -100 + input[i] # Start

        # Get maximum mood.
        # i-3 gets included only if nonnegative.
        return input[i] + max(dp(i-1), dp(i-2), *[dp(i-3)]*(dp(i-3) >= 0))

    # Build cache
    for k in range(len(input)): dp(k)
        
    print(dp(len(input) - 1))

    
if __name__ == '__main__':
    main()