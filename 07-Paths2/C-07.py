# n is the number of junctions
# m is the number of roads
n, m = map(int, input().strip().split())

# fa[i] is the parent of junction i in the disjoint set
fa = [i for i in range(n + 1)]

# val[i] is 1 if road i is non-horrible, 0 otherwise
val = [0] * (m + 1)


# Find the representative of the set containing x
def find(x):
    # If x is the parent of itself, x is the representative
    # of its set.
    if fa[x] == x:
        return x

    # Otherwise, we recursively call find on the parent
    # of x and assign the result to the parent of x.
    # This is done to perform path compression, which
    # helps to reduce the time complexity of subsequent
    # calls to find on the same set.
    return find(fa[x])


# For each road, check if it connects two different
# connected components. If it does, merge the two
# connected components. Otherwise, the road must
# be part of a cycle and we mark it as "horrible".
for i in range(1, m + 1):
    u, v = map(int, input().strip().split())

    # Find the representatives of the sets containing
    # u and v.
    u = find(u)
    v = find(v)

    # If the representatives are different, the road
    # connects two different connected components,
    # so we merge them by assigning the representative
    # of one of the sets as the parent of the other.
    if u != v:
        fa[u] = v

        # Mark the road as non-horrible
        val[i] = 1

# Count the number of non-horrible roads
num_non_horrible_roads = 0
for i in range(1, m + 1):
    if val[i]:
        num_non_horrible_roads += 1

# Print the number of non-horrible roads
print(num_non_horrible_roads)

# Print the indices of the non-horrible roads
for i in range(1, m + 1):
    if val[i]:
        print(i, end=" ")
print()
