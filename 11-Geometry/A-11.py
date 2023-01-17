def main() -> None:
    # Read from stdin.
    a, b, c, r = map(int, open(0).read().split())

    n_vec = complex(a, b)
    n0_vec = n_vec / abs(n_vec)

    # S: point on the original line
    try:
        S = complex(0, -c / b)
    except ZeroDivisionError:
        S = complex(-c / a, 0)

    # R, Q: points with distance r parallel to original line
    R = S + r * n0_vec
    Q = S - r * n0_vec

    # Same normal vector, new point.
    print(*["{:.9f}".format(i) for i in [a, b, -(a * R.real + b * R.imag)]])
    print(*["{:.9f}".format(i) for i in [a, b, -(a * Q.real + b * Q.imag)]])


if __name__ == "__main__":
    main()
