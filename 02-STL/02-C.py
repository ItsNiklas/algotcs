def main() -> None:
    # Read from stdin as integers.
    input = [map(int, x.split()) for x in open(0)]
    
    # Sort.
    print(*sorted(input[1], reverse = True))
    
if __name__ == '__main__':
    main()