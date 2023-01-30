def kmp_search(α, β):
    # The two strings to be matched with Knuth-Morris-Pratt.
    n, m = len(α), len(β)
    lps = [0] * m
    j = 0

    # Calculate lps list
    compute_lps(β, m, lps)
    i = 0
    positions = []
    # Main KMP
    while i < n:
        if β[j] == α[i]:
            i += 1
            j += 1
        if j == m:
            positions.append(i - j + 1)
            j = lps[j - 1]
        elif i < n and β[j] != α[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions


def compute_lps(β, m, lps):
    # Calculate the longest proper prefix which is also a suffix in β.
    length = 0
    i = 1
    while i < m:
        if β[i] == β[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


a, b = open(0).read().split()
res = kmp_search(a.strip(), b.strip())
print(len(res))
print(*sorted(res))
