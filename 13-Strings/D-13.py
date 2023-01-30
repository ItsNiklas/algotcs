def count_unique_substrings(s):
    n = len(s)

    # Create the suffix array with indices and sort lexographically.
    suffix_array = [(s[i:], i) for i in range(n)]
    suffix_array.sort()

    # Count unique substrings.
    # Iterate over suffix_array and compare with previous, find length of
    # their longest common prefix (which is the maximum number of characters
    # that are common)
    count = 0
    for i in range(1, n):
        length = 0
        for x, y in zip(suffix_array[i-1][0], suffix_array[i][0]):
            if x == y:
                length += 1
            else:
                break
        count += n - suffix_array[i][1] - length
    # Remove empty substrings (-n) and add the whole string (+1)
    return count - n + 1

print(count_unique_substrings(open(0).read()))