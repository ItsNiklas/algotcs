def main() -> None:
    # Read from stdin.
    input = [list(map(int, x.split())) for x in open(0)][1]
    N = len(input)

    # DP on intervals:
    # dp[i][j] = maximum energy generated using only stars i to j.
    dp = [[0] * N for _ in range(N)]

    for length in range(N):
        for i in range(N-length):
            j = i + length
            # Slide cutoff s through the interval to find all possible splits.
            # Add energy for exploding star s to left and right subintervals.
            # Default case if no explosions are possible (two stars).
            # [i ---s---> j]
            dp[i][j] = max(
                [dp[i][s] + dp[s][j] + input[i] * input[j] for s in range(i+1, j)],
                default = dp[i][j]
            )

    # Print maximum energy considering all stars.
    print(dp[0][-1])


if __name__ == '__main__':
    main()