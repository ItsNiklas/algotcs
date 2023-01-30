S = ""

# The trivial solution is sufficent in this problem configuration.
for line in open(0):
    line = line.split()
    if line[0] == "A":
        S += line[1].casefold()
    elif line[0] == "?":
        print("YES" if line[1].casefold() in S else "NO")

