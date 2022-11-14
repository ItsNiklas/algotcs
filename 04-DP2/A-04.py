from functools import lru_cache


def main() -> None:
    # Read from stdin.
    n = int(*open(0)) + 1

    # The sequence questioned is A001906.
    # F(2n) = bisection of Fibonacci sequence a(n) = 3*a(n-1) - a(n-2).
    @lru_cache(None)
    def a(n): return n if n <= 1 else 3 * a(n-1) - a(n-2)

    print(a(n))

    # O(1) Solution:
    # This has a closed-form solution with the recursion resolved by Luschny, 2022.
    # Floating point-precision is not good enough after n > 40, however.
    # https://oeis.org/A001906
    # print(round(2 * math.sinh(2 * n * math.asinh(1/2)) / math.sqrt(5)))


if __name__ == '__main__':
    main()