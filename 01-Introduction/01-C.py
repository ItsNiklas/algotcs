def main() -> None:
    # Read from stdin.
    input = [x.split() for x in open(0)]
    
    # Height of the flood in cm.
    flood = int(input[0][1])
    
    # Find buoys which need longer chains, because height < flood.
    # Result needs one-indexing.
    print(*[i for i, h in enumerate(input[1], 1) if int(h) < flood])
    
if __name__ == '__main__':
    main()