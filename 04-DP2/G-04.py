from math import hypot as norm


def main() -> None:
    # Read all problems from stdin in a weird format.
    input = [list(map(int, x.split())) for x in open(0)]
    inputs = list()
    for token in input:
        if token == [0]: break
        # Include start and end checkpoints.
        elif len(token) == 1: inputs.append([[0,0,0], [100,100,0]])
        else: inputs[-1].insert(-1, token)


    for input in inputs:
        # Find route with minimal penalty.
        # dp[i] is the minimal penalty when reaching point i.
        N = len(input)
        dp = [float("inf")] * N
        dp[0] = 0

        for i in range(1, N):
            x, y, p = input[i]
            # Count penalty sum on the fly, otherwise program is O(N³).
            psum = 0
            for j in reversed(range(i)):
                xn, yn, pn = input[j]
                # Skipping an increasing amount of elements, find minima of all.
                # Minimal penalty up to j + distance to point + penalties + capturing time.
                dp[i] = min(dp[i], dp[j] + norm(xn - x, yn - y) + psum + 1)
                psum += pn

        # Output the smallest score for the course up to the end,
        # with precision 10⁻⁶.
        print(f"{dp[-1]:.7f}")


if __name__ == '__main__':
    main()