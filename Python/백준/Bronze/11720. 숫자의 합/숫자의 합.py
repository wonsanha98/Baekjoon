N = int(input())
num = int(input())
sum = 0 

while 0 < N:
    sum += num % 10
    N -= 1
    num //= 10

print(sum)