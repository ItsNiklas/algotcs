from collections import deque


def main() -> None:
    # Read from stdin.
    fd = open(0)
    a, b = map(int, fd.readline().split())
    n = int(fd.readline())

    leafs = list()

    for _ in range(n):
        c, d, e = map(int, fd.readline().split())
        leafs.append((complex(c, d), e))

    d = int(fd.readline())

    # Set up adjacency dictionary
    adj = {i: list() for i in range(n)}

    # Leaf indices that can be reached from outside
    start_leafs = list()

    distances = [float("inf")] * (n + 1)

    for i in range(n):
        A, r1 = leafs[i]

        if A.real - r1 - d <= 0 or A.real + r1 + d >= a or A.imag - r1 - d <= 0 or A.imag + r1 + d >= b:
            start_leafs.append(i)
            distances[i] = 0

        for j in range(i + 1, n):
            # Calculate required jumping distance between two lilies.
            B, r2 = leafs[j]

            dist = abs(B - A) - r1 - r2
            if dist > d:
                # Too far.
                continue
            elif dist <= 0:
                # Can walk.
                adj[i].append((j, 0))
                adj[j].append((i, 0))
            else:
                # Must jump (weight 1).
                adj[i].append((j, 1))
                adj[j].append((i, 1))

    # BFS 0-1
    # Run BFS from edge leaves in towards the center.
    q = deque(start_leafs)

    while q:
        vertex = q.popleft()

        if vertex == n - 1:
            # Ball found.
            # Correct distance is already
            # calculated at this point.
            print(distances[vertex] + 1)
            return

        for e, cost in adj[vertex]:
            if distances[vertex] + cost < distances[e]:
                distances[e] = distances[vertex] + cost

                if cost == 1:
                    q.append(e)
                else:
                    q.appendleft(e)

    # All leaves searched, ball not reachablea
    print(":(")


if __name__ == "__main__":
    main()
