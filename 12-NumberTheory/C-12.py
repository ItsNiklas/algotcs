# Solution is n - 1 - phi(n), given in:
#   OEIS-A219428 (https://oeis.org/A219428)
# where phi is Euler's Totient Function.

# Implementation is O(√n).
def euler_totient(n):
    phi = n

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            phi -= phi // i
    if n > 1:
        phi -= phi // n

    return phi


fd = open(0)
_ = fd.readline()
for n in map(int, fd.read().split()):
    print(n - 1 - euler_totient(n) if n > 1 else 0)
