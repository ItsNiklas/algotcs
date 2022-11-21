from collections import deque


def main() -> None:
    # Read from stdin.
    input = [map(int, x.split()) for x in open(0)]
    V, E = input[0]

    # Create undirected Adjacency list.
    graph = {v+1 : set() for v in range(V)}
    all = {v+1 for v in range(V)}
    for u, v in input[1:]:
        graph[u].add(v); graph[v].add(u)

    # BFS.
    def bfs(root):
        # Initialize set and queue.
        from collections import deque
        visited, q = {root}, deque([root])

        while q:
            vertex = q.popleft()
            for next in graph[vertex]:
                if next not in visited:
                    visited.add(next)
                    q.append(next)
        return visited

    # Count components of connectivity k.
    k = 0
    while all:
        all -= bfs(all.pop()); k += 1

    # Result formula.
    print(E - V + k)


if __name__ == '__main__':
    main()