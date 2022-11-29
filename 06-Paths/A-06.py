from collections import deque


def main() -> None:
    # Read from stdin as a generator.
    input = (x.split() for x in open(0))
    # Number of Rooms, Doors
    V, E = map(int, next(input)) 

    # Create directed Adjacency list.
    graph = [set() for _ in range(V+1)]
    for u, v, l in input:
        graph[int(u)].add((int(v), 1 if l == 'l' else 0))

    # BFS 0-1.
    # Implemented with a deque.
    distances = [float('inf')] * (V+1)
    distances[1] = 0
    q = deque([1])

    while q:
        vertex = q.popleft()
        
        if vertex == V:
            # Exit found.
            # Correct distance is already
            # calculated at this point.
            print(distances[vertex])
            return
            
        for e, cost in graph[vertex]:
            if distances[vertex] + cost < distances[e]:
                distances[e] = distances[vertex] + cost
                
                if cost == 1: q.append(e)
                else: q.appendleft(e)

    # No exit found.
    print(-1)


if __name__ == '__main__':
    main()