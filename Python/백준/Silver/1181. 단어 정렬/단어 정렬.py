import sys

N = int(sys.stdin.readline())

strs = []*N

for i in range(N):
    str = sys.stdin.readline()
    strs.append(str)

sort_strs = list(set(strs))

sort_strs.sort()
sort_strs.sort(key = lambda x: len(x))


for i in sort_strs:
    print(i, end="")