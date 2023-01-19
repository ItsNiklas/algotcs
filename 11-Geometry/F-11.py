def dot(x: complex, y: complex) -> float:
    return (x.conjugate() * y).real


def cross(x: complex, y: complex) -> float:
    return (x.conjugate() * y).imag


def project(A: complex, B: complex, Pt=complex(0, 0)):
    # Project point onto segment [A, B]
    Ad = B - A

    t = dot(Pt - A, Ad) / dot(Ad, Ad)

    if not 0 < t < 1:
        return None
    return A + t * Ad


def intersect_lines(Ad: complex, As: complex, Bd: complex, Bs: complex):
    if cross(Ad, Bd) == 0:
        # Parallel
        if cross(Ad, As - Bs) == 0:
            # But on the same axis, return any intersection point.
            return Bs
        return False
    # Intersection point
    return Bs + cross(Ad, As - Bs) / cross(Ad, Bd) * Bd


def intersect_segments(Ad: complex, As: complex, Bd: complex, Bs: complex):
    # Segment from As to As + Ad
    p = intersect_lines(Ad, As, Bd, Bs)
    if not p:
        return False

    # Check if intersection lies inside the segments of both lines
    l1 = dot(p - As, Ad) / dot(Ad, Ad)
    l2 = dot(p - Bs, Bd) / dot(Bd, Bd)

    return 0 <= l1 <= 1 and 0 <= l2 <= 1


def main() -> None:
    # Read from stdin.
    fd = open(0)
    _ = fd.readline()
    x0, y0 = map(int, fd.readline().split())

    mirrors = list()

    # Read all mirrors, moved to be centered around 0, 0 (forced origin).
    for line in fd.readlines():
        a, b, c, d = map(int, line.split())
        A = complex(a - x0, b - y0)
        B = complex(c - x0, d - y0)
        mirrors.append((A, B))

    # Mirror: Segment A to B
    # Iterate over mirrors:
    for A, B in mirrors:
        P = project(A, B)

        if P:
            # Mirror is angled correctly.
            # But is there another mirror blocking it?
            # Check for intersection of any [X, Y] and [0, P]
            for X, Y in mirrors:
                if X == A and Y == B: continue
                if intersect_segments(P - 0, 0, Y - X, X):
                    break
            else:
                # No breaks, working mirror found.
                print(1)
                return

    print(0)
    return


if __name__ == "__main__":
    main()
