def main() -> None:
    # Read from stdin.
    mountain = [list(map(int, x.split())) for x in open(0)][1:]

    for level_id in range(1, len(mountain)):
        for slope_id in range(level_id + 1):
            # Iterate over all slopes.
            # For each slope, determine max of parents, if they exist.
            a = mountain[level_id - 1][slope_id - 1] if 0 <= slope_id - 1 < level_id else float('-inf')
            b = mountain[level_id - 1][slope_id] if 0 <= slope_id < level_id else float('-inf')

            # Write into cache.
            mountain[level_id][slope_id] += max(a, b)

    # Get maximum score at the lowest level.
    print(max(mountain[-1]))

    
if __name__ == '__main__':
    main()