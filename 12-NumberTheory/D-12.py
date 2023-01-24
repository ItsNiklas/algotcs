from math import gcd
from functools import reduce

# No clue why this works, see:
# https://math.stackexchange.com/questions/2422212
def find_common_remainder(numbers):
    numbers.sort()
    numbers = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    return reduce(gcd, numbers)


for line in open(0):
    ints = list(map(int, line.split()))[:-1]
    print(find_common_remainder(ints)) if len(ints) != 0 else exit(0)

