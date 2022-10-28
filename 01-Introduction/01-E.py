def squabbits(s: int) -> int:
    # Described behaviour is quivalent to quadratic growth:
    return (s+1)**2


def main() -> None:
    # Read from stdin.
    input = [int(x) for x in open(0)]
                
    # Execute function on every line after the first.
    # Pretty print.
    print(*[squabbits(x) for x in input[1:]], sep = '\n')


if __name__ == '__main__':
    main()