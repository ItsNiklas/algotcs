def dot(x: complex, y: complex) -> float:
    return (x.conjugate() * y).real


def cross(x: complex, y: complex) -> float:
    return (x.conjugate() * y).imag


def closest_distance(As, Ad, Bs, Bd) -> float:
    dx = Bs.real - As.real
    dy = Bs.imag - As.imag
    det = cross(Bd, Ad)

    u = dy * Bd.real - dx * Bd.imag
    v = dy * Ad.real - dx * Ad.imag

    if det == 0:
        # Parallel: But is there a collision?
        if u == 0 and v == 0:
            # On same line, but is there a collision?

            if Bd == Ad:
                # Yes, because they point in the same direction.
                return 0

            else:
                # Maybe, if ray A hits Bs.
                # As + t * Ad = Bs
                if Ad.real != 0:
                    ta = (Bs.real - As.real) / Ad.real
                else:
                    ta = (Bs.imag - As.imag) / Ad.imag

                if ta > 0:
                    # Ray will hit B.
                    return 0
                else:
                    # No - On the same axis, but shooting in different directions.
                    return abs(As - Bs)
        else:
            # True Parallel.
            return abs(As - Bs)

    elif u * det < 0 or v * det < 0:
        # No collision.

        # calculate the distance between the projection and the starting point of ray1
        t = dot(Bs - As, Ad) / dot(Ad, Ad)
        proj1 = As + t * Ad
        distance1 = abs(Bs - proj1) if t >= 0 else abs(Bs - As)

        # calculate the distance between the projection and the starting point of ray2
        t = dot(As - Bs, Bd) / dot(Bd, Bd)
        proj2 = Bs + t * Bd
        distance2 = abs(As - proj2) if t >= 0 else abs(As - Bs)

        return min(distance1, distance2)
    else:
        # collision:
        return 0


def main() -> None:
    # Read from stdin.
    a, b, c, d, e, f, g, h = map(int, open(0).read().split())

    As = complex(a, b)
    Ad = complex(c, d) - As
    Ad = Ad / abs(Ad)  # Norm

    Bs = complex(e, f)
    Bd = complex(g, h) - Bs
    Bd = Bd / abs(Bd)  # Norm

    print("{:.6f}".format(closest_distance(As, Ad, Bs, Bd)))


if __name__ == "__main__":
    main()
