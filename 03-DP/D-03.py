from functools import lru_cache
from itertools import count, takewhile


############ !
# This is too slow for the judge in any shape or form I tried.
# Even though it is in the lowest complexity class possible,
# it is still 15x too slow on the largest test case.
# Still included, because it looks neat. Refer to the cpp variant.
############


def main() -> None:
    # Read from stdin.
    input = [int(x) for x in open(0)][1:]

    # Get applicable pyramid sizes for input.
    # Taking from an infinite generator until pyramids are large enough.
    # Thanks OEIS/A000292, Triangular pyramidal numbers.
    pyramids = list(takewhile(lambda n : n <= max(input), (n*(n+1)*(n+2)//6 for n in count(1))))
    
    # Memoization à la Python.
    # Using the Least Recently Used Cache decorator.
    @lru_cache(None)
    def dp(m : int) -> int:
        # This is identical to the coin change problem.
        return min([1 + dp(m - p) for p in pyramids if m - p >= 0], default = 0)

    # Fill cache
    for m in range(1, max(input)): dp(m)
        
    # Pretty print results.
    print(*[dp(m) for m in input], sep = '\n')


if __name__ == '__main__':
    main()