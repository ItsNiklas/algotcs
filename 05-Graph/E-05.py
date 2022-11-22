from itertools import product


def main() -> None:
    # Read from stdin.
    M, N, p, q, x, y, xn, yn = map(int, open(0).read().split())

    # Special case, no moves needed.
    if x == xn and y == yn: print(0); return

    # Get set of possible movements to iterate over.
    delta = set(product([-p, p], [-q, q])) | set(product([-q, q], [-p, p]))

    # Build depth dictionary. Goal has -1 in case it is never reached during
    # the search.
    depth = {(x, y) : 0, (xn, yn) : -1}

    # BFS.
    def bfs(root):
        # Initialize set and queue.
        from collections import deque
        visited, queue = {root}, deque([root])

        while queue:
            vertex = queue.popleft()
            # Calculate all possible locations to jump to.
            for next in [(vertex[0] + dx, vertex[1] + dy) for dx, dy in delta]:
                # Check out-of-bounds jumps.
                if not 0 < next[0] <= M or not 0 < next[1] <= N: continue
                if next not in visited:
                    # One more move to the next square.
                    depth.update({next : depth[vertex] + 1})
                    # Goal node reached.
                    if next == (xn, yn): return
                    visited.add(next)
                    queue.append(next)

    # Run to fill depth map.
    bfs((x,y))

    # Print depth at goal node.
    print(depth.get((xn, yn)))


if __name__ == '__main__':
    main()