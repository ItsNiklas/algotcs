def main() -> None:
    # Read from stdin.
    input = [x.split() for x in open(0)]
    
    # Get only queue lines, by starting at index 2 and incrementing by 2.
    # Reverse each queue via slicing.
    rev = [q[::-1] for q in input[2::2]]
    
    # Pretty print.
    print(*[' '.join(x) for x in rev], sep = '\n')
    
if __name__ == '__main__':
    main()