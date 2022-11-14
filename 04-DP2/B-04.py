def main() -> None:
    # Read from stdin.
    input = [map(int, x.split()) for x in open(0)][1:]
    N = len(input); C = 3001

    # DP cache, one for each row in the parking lot.
    # This is similar to the Knapsack problem.
    dp_narrow = [[0] * C for _ in range(N+1)]
    dp_wide   = [[0] * C for _ in range(N+1)]

    # Iterate over all cars, filling up the arrays.
    for i, (l, w, a) in enumerate(input):
        # Profit for a visitors.
        p = 150 if a <= 2 else a * 100

        # Fill, considering a parking lot of size c.
        for c in range(C):
            # Default case.
            dp_wide[i+1][c] = dp_wide[i][c]
            dp_narrow[i+1][c] = dp_narrow[i][c]

            # Out of bounds, or car too large.
            if c < w or l > 60: continue

            # Place new car in the respective lot.
            if l <= 40: dp_narrow[i+1][c] = max(dp_narrow[i+1][c], dp_narrow[i][c - w] + p)
            else: dp_wide[i+1][c] = max(dp_wide[i+1][c], dp_wide[i][c - w] + p)

    # Print final result.
    print(dp_narrow[-1][-1] + dp_wide[-1][-1], "$", sep="")


if __name__ == '__main__':
    main()