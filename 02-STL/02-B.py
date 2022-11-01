def main() -> None:
    # Read from stdin. Strip newline. Reverse the line. Reverse the lines.
    input = [x.rstrip()[::-1] for x in open(0)][::-1]
    
    # Pretty print.
    print(*input, sep = '\n')
    
if __name__ == '__main__':
    main()