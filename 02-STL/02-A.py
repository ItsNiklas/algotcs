def main() -> None:
    # Read from stdin. Write count directly to buffer.
    input = [x.count('a') for x in open(0)]
    
    # Inline-if.
    print("go" if input[0] >= input[1] else "no")
    
if __name__ == '__main__':
    main()