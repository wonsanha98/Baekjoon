# 원판의 갯수 n, 시작하는 봉 a, 끝나는 봉 b

def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6 -a -b)

    print(f"{a} {b}")

    if n > 1:
        hanoi(n-1, 6 -a -b, b)

n = int(input())
num = 2**n -1
print(num)

if n <= 20:
    hanoi(n, 1, 3)