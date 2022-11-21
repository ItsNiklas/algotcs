from itertools import chain


def main() -> None:
    # Read from stdin.
    input = [list(map(int, x.split())) for x in open(0)]

    for A in input[2::2]:
        # Find length of the longest convex subsequence in A.
        N = len(A)
        dp = [[2] * N for _ in range(N)]

        for i in range(N):
            for j in range(i+1, N):
                # dp[i][j] is the length of the longest convex subsequence
                # ending in elements at i and j.
                # Add one more if convex condition on i and j is met.
                # Don't change if matching element is found in comprehension.
                dp[i][j] = max(
                    [dp[k][i] + 1 for k in range(i) if 2 * A[i] <= A[k] + A[j]],
                    default = dp[i][j]
                )

        # Flatten list and get maximum.
        print(max(chain(*dp)))


if __name__ == '__main__':
    main()