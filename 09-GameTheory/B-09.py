# Huge shoutout to
# Duchêne, Eric, et al. "Partizan Subtraction Games." arXiv preprint
# https://arxiv.org/pdf/2101.01595.pdf
# I could not have solved this without the paper.
# This particular case is covered in Lemma 15, where S_L = {1,...,k}, |S_R| = k.
# With c = 1, Left is WD (Weakly Dominating) as S_R = {1+c,...,k+c}.

fd = open(0)
_ = int(fd.readline())

# A recusive implementation consists of the following, but needs
# DP-Like cache-filling and is obvioulsy brute-force:
#
# A = range(1, k + 1)  # You (turn 0)
# B = range(2, k + 2)  # Friend (turn 1)
#
#
# @lru_cache(None)
# def play(heap: int, turn: int) -> int:
#     if heap == 0:
#         return turn
#
#     for x in B if turn else A:
#         if x > heap:
#             continue
#         result = play(heap - x, int(not turn))
#         if result != turn:
#             return result
#
#     return turn


# But...
# This problem is fully solved and the game is (always) purely periodic, with
# the period being
#     P L^c N^k.
# For this particular problem this reduces to:
#     L L R^k.
# And the element can be queried easily.
# Now test all possible moves by imitating an R start with reduced heap sizes.
# Starting at the largest possible removal size k, iterate to find winning
# state:


# def play_r(n: int, k: int) -> bool:
#     return n % (k + 2) <= 1
#
# for m in reversed(range(1, k + 1)):
#     if play_r(n - m, k):
#         print(m)
#         break
# else:
#     print(0)


# However, this is too slow. There must be another optimization.
# L locations are at indices:
# (k+2)*N, (k+2)*N+1  |  for all N.
# The result of the modulo operation instantly gives the offset to
# get to the next winning state L, which can be even more simplified.
# This is the final O(1) solution:


for line in fd:
    n, k = map(int, line.strip().split())

    o = (n - k) % (k + 2) - 2
    print(k if o < 0 else o)
