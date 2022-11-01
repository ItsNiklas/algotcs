def inspection(holding_area) -> int:
    # Returns the index of median diameter among all cookies currently in the holding area
    n = len(holding_area)
    
    if n % 2 == 1: return (n+1) // 2 # odd number of cookies in the holding area
    else: return n // 2 + 1          # even number of cookies in the holding area       


def main() -> None:
    # Read from stdin.
    input = (x.rstrip() for x in open(0))
    
    # 'Sorted' list
    holding_area = list()
    
    # Loop over instructions.
    for c in input:
        if c == '#':
            # Print and delete by index for O(1) (?)
            idx = inspection(holding_area) - 1
            print(holding_area[idx])
            holding_area.pop(idx)
        else:
            # Insert into holding area.
            holding_area.append(int(c)); holding_area.sort()
    
if __name__ == '__main__':
    main()