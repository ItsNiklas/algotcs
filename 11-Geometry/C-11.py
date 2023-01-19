def dot(x: complex, y: complex) -> float:
    return (x.conjugate() * y).real


def cross(x: complex, y: complex) -> float:
    return (x.conjugate() * y).imag


def intersect_lines(Ad: complex, As: complex, Bd: complex, Bs: complex):
    if cross(Ad, Bd) == 0:
        # Parallel
        if cross(Ad, As - Bs) == 0:
            # But on the same axis, return any intersection point.
            return Bs
        return False
    # Intersection point
    return Bs + cross(Ad, As - Bs) / cross(Ad, Bd) * Bd


def intersect_segments(Ad: complex, As: complex, Bd: complex, Bs: complex):
    # Segment from As to As + Ad
    p = intersect_lines(Ad, As, Bd, Bs)
    if not p:
        return False

    # Check if intersection lies inside the segments of both lines
    l1 = dot(p - As, Ad) / dot(Ad, Ad)
    l2 = dot(p - Bs, Bd) / dot(Bd, Bd)

    return 0 <= l1 <= 1 and 0 <= l2 <= 1


# Parents array to store the parent of each node
# Initially, each node is a parent of itself
parents = [i for i in range(2000)]
# Rank array to store the rank of each node
# Initially, each node has rank 0
ranks = [0 for _ in range(2000)]

# Cut arrays.
cuts = []
mins = []
maxs = []


# Function to merge two nodes
def union(node1, node2):
    # Find the parent of each node
    parent1 = find(node1)
    parent2 = find(node2)

    # If the nodes have the same parent, they are already in the same set
    if parent1 == parent2:
        return False
    # Otherwise, set the parent of the second node as the parent of the first node
    if ranks[parent1] > ranks[parent2]:
        parents[parent2] = parent1
    else:
        parents[parent1] = parent2
        if ranks[parent1] == ranks[parent2]:
            ranks[parent2] += 1
    return True


# Function to find the parent of a given node
def find(node):
    # If the given node is the parent of itself, return it
    if parents[node] == node:
        return node
    # Otherwise, recursively find the parent of the given node (Compression)
    parents[node] = find(parents[node])
    return parents[node]


def main() -> None:
    # Read from stdin.
    fd = open(0)
    _, w = map(int, fd.readline().split())

    # Read inputs.
    for line in fd:
        a, b, c, d = map(int, line.split())
        A = complex(a, b)
        B = complex(c, d)

        # "Cut" is a point, skip to avoid ZeroDivisionError.
        if A == B:
            continue

        # Cut already cuts the paper.
        if min(b, d) <= 0 and max(b, d) >= w:
            print(0)
            return

        # Clipped inputs
        mins.append(max(0, min(b, d)))
        maxs.append(min(w, max(b, d)))
        cuts.append((A, B))

    N = len(cuts)

    for i in range(N):
        for j in range(i + 1, N):
            # Pairwise iteration.
            A, B = cuts[i]
            X, Y = cuts[j]
            P = intersect_segments(B - A, A, Y - X, X)

            # Check if P exisits and inbounds.
            if not P or not 0 <= P.imag <= w:
                continue

            # Cuts are connected:
            max_i = maxs[find(i)]
            max_j = maxs[find(j)]
            min_i = mins[find(i)]
            min_j = mins[find(j)]

            # New connection will cut paper.
            if max(max_i, max_j) == w and min(min_i, min_j) == 0:
                print(0)
                return

            # Merge connected components, update representatives' min/max.
            if union(i, j):
                maxs[find(i)] = max(max_i, max_j)
                mins[find(i)] = min(min_i, min_j)

    print(1)

if __name__ == "__main__":
    main()
