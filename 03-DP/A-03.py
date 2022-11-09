from functools import lru_cache


def main() -> None:
    # Read from stdin.
    input = [list(x.rstrip()) for x in open(0)][1]

    # Memoization à la Python.
    # Using the Least Recently Used Cache decorator.
    @lru_cache(None)
    def dp(i: int) -> int:
        if i == 0: return 0 # Starting spot
        if i < 0 or input[i] == "w": return -1 # Out of bounds or wolves.

        # Previous maximum amout of grass.
        prev = max(dp(i-1), dp(i-3), dp(i-5)) 
        
        # Add 1 if Grass at current location, but only if accessible.
        return prev + (input[i] == "\"" if prev != -1 else 0)

    # Build cache
    for i in range(len(input)): dp(i)
        
    print(dp(len(input) - 1))

    
if __name__ == '__main__':
    main()