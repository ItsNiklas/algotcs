def main() -> None:
    # Read from stdin.
    input = [x.split() for x in open(0)][0]
    
    # The integer sum of A and B.
    a = int(input[0]); b = int(input[1])
    print(a + b)
    
if __name__ == '__main__':
    main()