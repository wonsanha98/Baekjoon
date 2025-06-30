# 영어 소문자만 기록하는 편집기, 최대 600,000
import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())

    elif cmd[0] == 'B':
        if left:
            left.pop()

    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left + list(reversed(right)))) 