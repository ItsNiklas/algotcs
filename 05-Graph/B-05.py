def main() -> None:
    # Read from stdin.
    input = [list(map(int, x.split())) for x in open(0)][1:]

    # Create Adjacency list.
    graph = {v+1 : set() for v in range(len(input) + 1)}
    for i, (p, h) in enumerate(input):
        graph[p].add(i+2)

    # Depth to i+1 is h, dp-esque.
    depth = [0, 0] + [h for p, h in input]

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
                    # Custom:
                    # Increase depth reached at plateau next accordingly.
                    depth[next] += depth[vertex]
        return visited

    # Run to fill depth map.
    bfs(1)

    # Print maximum depth reached.
    print(max(depth))


if __name__ == '__main__':
    main()