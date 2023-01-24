from functools import reduce
from math import gcd

# Read candy values
fd = open(0)
_ = fd.readline()
candies = map(int, fd.read().split())

# Compute gcd of all values, -1 because brother is invited by default.
print(reduce(gcd, candies) - 1)
