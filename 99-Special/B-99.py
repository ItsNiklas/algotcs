def main() -> None:
    fd = open(0)
    N, _ = map(int, fd.readline().split())
    N += 1

    fr = {a: 0 for a in range(1, N)}
    to = {a: 0 for a in range(1, N)}

    for line in fd.readlines():
        x, y = map(int, line.split())
        fr[x] += 1
        to[y] += 1

    print(sum(filter(lambda v: v > 0, [to[x] - fr[x] for x in range(1, N)])))


if __name__ == '__main__':
    main()
