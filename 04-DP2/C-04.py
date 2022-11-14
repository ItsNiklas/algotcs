def main() -> None:
    # Read from stdin. Weird switching input format.
    input = [list(map(int, x.split())) for x in open(0)][1:]
    input = [x for sublist in input for x in sublist]
    N = len(input)

    # Two different alternating sequences possible.
    dp = [1 for _ in range(N)]
    dq = [1 for _ in range(N)]

    # Longest Alternating Subsequence by template.
    for i in range(N):
        for j in range(i):
            if input[j] < input[i]: dp[i] = max(dp[i], dq[j] + 1)
            if input[j] > input[i]: dq[i] = max(dq[i], dp[j] + 1)

    print(max(dp + dq))


if __name__ == '__main__':
    main()