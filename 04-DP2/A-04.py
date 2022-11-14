import math

def main() -> None:
    # Read from stdin.
    N = int(*open(0)) + 1

    # O(1) Solution:
    # The sequence questioned is A001906 F(2n) = bisection of Fibonacci sequence.
    # This includes a closed-form solution by Luschny, 2022.
    # https://oeis.org/A001906

    print(round(math.sinh(2 * N * math.asinh(1/2)) / math.sqrt(5/4)))


if __name__ == '__main__':
    main()