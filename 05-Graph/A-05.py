def main() -> None:
    # Read from stdin.
    input = [map(int, x.split()) for x in open(0)]
    V, E = input[0]

    # Create undirected Adjacency list.
    graph = {v+1 : set() for v in range(V)}
    for u, v in input[1:]:
        graph[u].add(v); graph[v].add(u)

    # DFS.
    def dfs(vertex, visited):
        if vertex not in visited:
            visited.add(vertex)
            for next in graph[vertex] - visited:
                dfs(next, visited)
            return visited

    # Only one large component or not?
    print("YES" if len(dfs(1, set())) == V else "NO")


if __name__ == '__main__':
    main()