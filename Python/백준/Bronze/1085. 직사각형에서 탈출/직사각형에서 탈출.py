import sys

x, y, w, h = sys.stdin.readline().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

if x > y:
    l = y
else:
    l = x

if l > w-x:
    l = w-x
if l > h-y:
    l = h-y

print(l)