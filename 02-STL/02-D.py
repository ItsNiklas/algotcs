def last_index(l, v: int) -> int:
    # Returns the last index of v in the already reversed l.
    # 0 as the default case.
    try:
        return len(l) - l.index(v)
    except ValueError:
        return 0
        

def main() -> None:
    # Read from stdin.
    input = list(open(0))
    hashes = list(map(int, input[1].split()))
    
    # Pretty print. Loop over all codes and compute last index of b.
    hashes.reverse()
    print(*[last_index(hashes, int(b)) for b in input[2:]], sep = '\n')
    
if __name__ == '__main__':
    main()