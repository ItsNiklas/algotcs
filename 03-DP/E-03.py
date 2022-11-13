from itertools import product


def main() -> None:
    # Read from stdin.
    input = [map(int, x.split()) for x in open(0)]
    N, M, _, H = input[0]

    # Initialize two grids.
    # One will store the cumulative damage to all towers accessing the field.
    # The other is our dp cache.
    dmg_grid = [[0] * N for _ in range(M)]
    dp_grid  = [[0] * N for _ in range(M)]

    # Calculate all tower damage,
    # adding their damage to each field in their radius and inbounds.
    for n, m, r, d in input[1:]:
        for i, j in product(range(-r,r+1), repeat = 2):
            if 0 <= m-1+i < M and 0 <= n-1+j < N:
                dmg_grid[m-1+i][n-1+j] += d

    # Dynamic Programming.
    # Fill cache from right to left, top to bottom, bottom to top. O(N*2M)
    for i_col in reversed(range(N-1)):
        for i_row in range(M):
            # Accept only moves from the right and above for now.
            # Store the minimal amount of damage up to this point in the grid.
            right = dp_grid[i_row][i_col+1] if i_col+1 < N else float('inf')
            up = dp_grid[i_row-1][i_col] if 0 <= i_row-1 else float('inf')
            dp_grid[i_row][i_col] = min(right, up) + dmg_grid[i_row][i_col]
            
        for i_row in reversed(range(M)):
            # Run back the calculation, now including a possible up path,
            # which was not computed before.
            down = dp_grid[i_row+1][i_col] if i_row+1 < M else float('inf')
            prev = dp_grid[i_row][i_col] - dmg_grid[i_row][i_col]
            dp_grid[i_row][i_col] = min(down, prev) + dmg_grid[i_row][i_col]

    # Run through left column to find minimal damage possible,
    # return 0 if dead.
    print(max(H - min([row[0] for row in dp_grid]), 0))


if __name__ == '__main__':
    main()