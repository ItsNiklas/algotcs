import copy


def main() -> None:
    # Read from stdin.
    input = [list(map(int, x.split())) for x in open(0)][1:]

    # Deepcopy to create our cache.
    output = copy.deepcopy(input)

    for level_id in range(1, len(input)):
        for slope_id in range(level_id + 1):
            # Iterate over all slopes.
            # For each slope, determine max of parents, if they exist.
            a = output[level_id - 1][slope_id - 1] if 0 <= slope_id - 1 < level_id else float('-inf')
            b = output[level_id - 1][slope_id] if 0 <= slope_id < level_id else float('-inf')

            # Write into cache.
            output[level_id][slope_id] += max(a, b)

    # Get maximum score at the the lowest level.
    print(max(output[-1]))

    
if __name__ == '__main__':
    main()