from collections import deque
from itertools import product


def main() -> None:
    # Read from stdin.
    input = [list(x.rstrip()) for x in open(0)]
    grid = input[1:]
    N, M = len(grid), len(grid[0])

    # Create neighbors function.
    def neighbors(loc):
        x, y = loc
        # Adjacent locations.
        nb = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        # Filter out of bounds and walls.
        nb = filter(lambda xy : 0 <= xy[0] < N and 0 <= xy[1] < M, nb)
        nb = filter(lambda xy : grid[xy[0]][xy[1]] != "#", nb)
        return nb

    # Cost function
    def cost(from_from_node, from_node, to_node):
        c = 0
        
        if grid[next[0]][next[1]] == "D":
            # Correct for starting direction: Right.
            dx, dy = to_node[0] - from_node[0], to_node[1] - from_node[1]
            if dx != 0: c += 1
            elif dy == 1: c += 2
                
        if from_from_node is None:
            return 1 + c # First move
        if to_node == from_from_node:
            return 3 + c # Turn around
            
        # Are we turning? Add one more to the cost.
        ddx, ddy = to_node[0] - from_from_node[0], to_node[1] - from_from_node[1]
        return (2 if ddx != 0 and ddy != 0 else 1) + c

    # Find start (C)
    start = [x for x in grid if "C" in x][0]
    start = (grid.index(start), start.index("C"))

    # BFS/Floodfill
    # Missing: Early stopping.
    # Initialize came_from/distance dict and queue.
    q = deque([start])
    distance = {start : {(None, 0)}}
    score = float("inf")

    while q:
        vertex = q.popleft()

        for next in neighbors(vertex):
            # We need per-parent distances because of turning cost.
            for parent, old_dist in distance[vertex]:
                new_dist = old_dist + cost(parent, vertex, next)

                # Add new connection.
                if next in distance:
                    distance[next].add((vertex, new_dist))
                else:
                    distance.update([(next, {(vertex, new_dist)})])
                    q.append(next)

                # Some goal found, new shortest path?
                if grid[next[0]][next[1]] == "D":
                    score = min(score, new_dist)

    # Output shortest path length if found.
    print(score) if score != float("inf") else print("IMPOSSIBLE")


if __name__ == '__main__':
    main()