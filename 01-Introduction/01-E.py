def main() -> None:
    # Read from stdin.
    input = [int(x) for x in open(0)]
                
    # Execute function on every line after the first.
    # Described behaviour is quivalent to quadratic growth.
    # Pretty print.
    print(*[(x+1)**2 for x in input[1:]], sep = '\n')


if __name__ == '__main__':
    main()