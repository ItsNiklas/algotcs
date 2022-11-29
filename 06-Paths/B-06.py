from queue import PriorityQueue


def main() -> None:
    # Read from stdin as a generator.
    input = (map(int, x.split()) for x in open(0))
    
    # States, Transitions, Finals
    S, T, F = next(input)
    finals = list(next(input))

    # Create directed Adjacency list.
    graph = [set() for _ in range(S+1)]
    for u, v, p in input:
        graph[u].add((v, p))

    # Djisktra. (optimized)
    # This includes the usage of a priority queue.
    dis = [float('inf')] * (S+1)
    dis[1] = 0;
    
    pq = PriorityQueue()
    pq.put((0, 1))

    while not pq.empty():
        d, vertex = pq.get()
        for n, cost in graph[vertex]:
            if d + cost < dis[n]:
                dis[n] = d + cost
                pq.put((d + cost, n))

    # Filter for final states.
    dis = [v if i in finals else float('inf') for i, v in enumerate(dis)]

    # Print minimal value and index if it exists.
    m = min(dis)
    print("IMPOSSIBLE") if m == float('inf') else print(m, dis.index(m))


if __name__ == '__main__':
    main()