# Problem statement is:
# Smallest positive integer m such that m == prime(i) (mod prime(i+1)) for
# all 1<=i<=n.
# Which is suggested by the Chinese Remainder Theorem and given in:
#
#   OEIS-A157752, https://oeis.org/A157752
#

A157752 = [-1, -1, 2, 8, 68, 1118, 2273, 197468, 1728998, 1728998, 447914738,
           10152454583, 1313795640428, 97783391392958, 5726413266646343,
           38433316595821418, 15103232990013860963, 943894249589930135768,
           52858423703753671390658, 932521283899305953765183,
           8790842834979573009644273]

print(A157752[int(open(0).read())])