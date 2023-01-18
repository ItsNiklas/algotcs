import math


def cross(x: complex, y: complex) -> float:
    return (x.conjugate() * y).imag


def main() -> None:
    # Read from stdin.
    fd = open(0)
    W, _ = map(int, fd.readline().split())

    lines = list()
    parallel = True

    for line in fd:
        a, b, c, d = map(int, line.split())
        A = complex(a, b)
        B = complex(c, d)

        # Check if same line is in list already.
        for X, Y in lines:
            if cross(A - B, X - Y) == 0:
                # Void identical lines:
                if cross(A - Y, X - B) == 0 and cross(A - X, Y - B) == 0:
                    break
            else:
                # Non-parallel line detected.
                parallel = False
        else:
            lines.append((A, B))

    p = len(lines)
    N = p + 1 if parallel else 2 * p  # No. Sectors with infinite area.

    if W <= N:
        print(0)
        return

    # We have to add lines...
    if parallel and N + 1 == W:
        # Now worth to upgrade equation
        print(1)
    else:
        # Already at better equation / Upgrade
        # delta lines = required lines if not par - current lines
        dp = math.ceil(W / 2) - p
        print(dp)


if __name__ == "__main__":
    main()
