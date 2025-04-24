import sys

t = sys.stdin.readline()
t = int(t)

for i in range(t):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a+b)