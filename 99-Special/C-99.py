from heapq import heappush, heappop


def main() -> None:
    fd = open(0)
    N, _ = map(int, fd.readline().split())

    adj = {a: [] for a in range(1, N + 1)}

    for line in fd:
        _, C, *stations = map(int, line.split())

        for a, b in zip(stations, stations[1:]):
            adj[a].append((b, C))
            adj[b].append((a, C))

    # Prim's Algorithm to find MST
    mst_sum = 0
    visited = {1}
    edges = []

    for neighbor, weight in adj[1]:
        heappush(edges, (weight, 1, neighbor))

    while edges:
        weight, u, v = heappop(edges)

        if v not in visited:
            visited.add(v)
            mst_sum += weight

            # push all edges of new vertex into the priority queue
            for neighbor, weight in adj[v]:
                if neighbor not in visited:
                    heappush(edges, (weight, v, neighbor))

    print(mst_sum)


if __name__ == '__main__':
    main()
