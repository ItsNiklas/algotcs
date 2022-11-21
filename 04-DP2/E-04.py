def main() -> None:
    # Read from stdin and sort. (!)
    # Then this turns into a subsequence problem where the proportion
    # of neighbors has to lie inside ]0.5, 2[.
    input = [sorted(list(map(int, x.split()))) for x in open(0)][1]
    N = len(input)

    dp = [1] * N

    for i in range(N):
        # Seating up to person i.
        # Add 1 if condition of new person is met.
        dp[i] = max(
            [dp[j] + 1 for j in range(i) if input[i] < 2 * input[j]],
            default = dp[i]
        )

    print(max(dp))


if __name__ == '__main__':
    main()