def kmp(s):
    # Use KMP to construct a partial match table fail.
    n = len(s)
    fail = [0] * n
    j = 0
    for i in range(1, n):
        while j and s[j] != s[i]:
            j = fail[j - 1]
        if s[j] == s[i]:
            j += 1
        fail[i] = j

    # After construction, the repeating substring is the last element
    # in the table.
    return fail[-1]

S = open(0).read().strip()
print(len(S) - kmp(S))