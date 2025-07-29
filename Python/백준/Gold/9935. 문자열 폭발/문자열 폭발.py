import sys
input = sys.stdin.readline

stack = []
text = input().rstrip()
bomb = input().rstrip()

for ch in text:
    stack.append(ch)
    if ch == bomb[-1] and len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")