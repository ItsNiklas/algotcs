from collections import deque
from itertools import product


def main() -> None:
    def print_g(g, p = None):
        if p is not None:
            for i in range(N):
                for j in range(M):
                    c = p.index((i, j)) if (i, j) in p else g[i][j]
                    print(c, end=" ")
                print()
        elif type(g) == dict:
            for i in range(N):
                for j in range(M):
                    c = g.get((i,j), -1)
                    print(c if c != -1 else grid[i][j], end=" ")
                print()
        else:
            for i in range(len(g)): print(*g[i], sep=" ")

    # Read from stdin.
    input = [list(x.rstrip()) for x in open(0)]
    grid = input[1:]
    N, M = len(grid), len(grid[0])

    # Create Adjacency list.
    def neighbors(loc):
        x, y = loc
        nb = [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]
        nb = filter(lambda xy : 0 <= xy[0] < N and 0 <= xy[1] < M, nb)
        nb = filter(lambda xy : grid[xy[0]][xy[1]] != "#", nb)
        return set(nb)

    graph = {location : neighbors(location) for location in product(range(N), range(M))}

    def cost(from_from_node, from_node, to_node):
        correction = 0
        if grid[next[0]][next[1]] == "D":
            # Correct for starting position: right.
            dx, dy = to_node[0] - from_node[0], to_node[1] - from_node[1]
            if dx == 0 and dy == 1:
                correction += 2
            elif dx == 0 and dy == -1:
                correction += 0
            else:
                correction += 1
        if from_from_node is None: return 1 + correction # First move
        if to_node == from_from_node: return 3 + correction # Turn around
        return 1 + (1 if to_node[0] != from_from_node[0] and to_node[1] != from_from_node[1] else 0) + correction

    # ?
    start = [x for x in grid if "C" in x]
    if not any(start):
        print("IMPOSSIBLE")
        return
    start = (grid.index(start[0]), start[0].index("C"))

    distance = {start: 0}

    # BFS.

    # Initialize came_from set and queue.
    visited, q = {x : set() for x in graph.keys()}, deque()
    visited[start].add(None)
    q.append(start)

    goal = None
    score = float("inf")

    while q:
        if goal is not None and max(distance.values()) > 3 * score:
            break
        vertex = q.popleft()

        for next in graph[vertex]:
            # We found a faster way to get to next?
            for parent in visited[vertex]:
                new_dist = distance[vertex] + cost(parent, vertex, next)
                if next in distance and new_dist == distance[next]:
                    # New entry direction
                    visited[next].add(vertex)
                if next not in distance or new_dist < distance[next]:
                    distance[next] = new_dist
                    visited[next].add(vertex)

                    # Some goal found
                    if grid[next[0]][next[1]] == "D" and new_dist < score:
                        score, goal = new_dist, next

                    # Missing: Early stopping
                    #if goal is None:
                    q.append(next)
    if goal is None: score, goal = -1, (-1, -1)

    ###

    print_g(distance)

    # Goal not reached
    if sum(goal) < 0:
        print("IMPOSSIBLE")
        return

    print(distance[goal])


if __name__ == '__main__':
    main()