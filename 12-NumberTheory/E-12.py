from itertools import count

# Approach:
# Calculate the highest power of K that divides N! using Legendre’s formula.
# The problem reduces to finding the highest power of K in N!.

N, K = map(int, open(0).read().split())

# Source:
# https://tutorialspoint.com/find-the-number-of-trailing-zeroes-in-base-b-representation-of-n-using-cplusplus

prime_factors = []
for i in count(2):
    # Calculate prime factors of base K along with occurences.
    if K == 1:
        break

    if K % i == 0:
        count = 0
        while K % i == 0:
            K = K // i
            count += 1

        prime_factors.append((i, count))

result = float('inf')
# Find the largest power of K that divides N!.
for i in range(len(prime_factors)):
    count = 0
    r, s = prime_factors[i]
    while r <= N:
        count += N // r
        r *= prime_factors[i][0]
    result = min(result, count // s)

print(result)
