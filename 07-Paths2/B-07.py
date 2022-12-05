# Store the input in variables n, m, p1 and p2
n, m, p1, p2 = map(int, input().split())

# Initialize the total amount of honey to 0
total_honey = 0

# Create a list of edges, where each edge is a tuple containing the coordinates
# of the two states and the weight of the edge
edges = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # Calculate the coordinates of the current state
        x1, y1 = i, j

        # Calculate the amount of honey required to connect the current state
        # to each of its neighbors
        for x2, y2 in [(i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j), (i + 1, j + 1)]:
            # Check if the neighbor is a valid state in the honeycomb
            if 1 <= x2 <= n and 1 <= y2 <= m:
                # Check if the neighbor has a smaller row and column index than
                # the current state, to avoid adding the same edge multiple times
                if x2 < x1 or (x2 == x1 and y2 < y1):
                    # Add the amount of honey required to connect the two states
                    # to the list of edges
                    weight = (x1 * x2 + p1 * y1 * y2) % p2
                    # Index = x * width + y
                    idx = (x1 - 1) * m + y1 - 1
                    idy = (x2 - 1) * m + y2 - 1
                    edges.append((idx, idy, weight))

# Sort the list of edges in ascending order of weight
edges.sort(key=lambda edge: edge[2])

# print(*edges, len(edges), sep='\n')

# Parents array to store the parent of each node
# Initially, each node is a parent of itself
parents = [i for i in range(n * m)]
# Rank array to store the rank of each node
# Initially, each node has rank 0
ranks = [0 for i in range(n * m)]


# Function to find the parent of a given node
def find(node):
    # If the given node is the parent of itself, return it
    if parents[node] == node:
        return node
    # Otherwise, recursively find the parent of the given node
    parents[node] = find(parents[node])
    return parents[node]


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

# Kruskal
for v, u, c in edges:
    if union(v, u):
        total_honey += c

# Output the total amount of honey
print(total_honey)
