import math

def prime(x):
    int(x)

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        
    return True

prime_nums = []

[prime_nums.append(i) for i in range(2, 10001) if prime(i)]

t = int(input())

for i in range(t):
    taget = int(input())
    min_prime = []

    a = 0
    b = len(prime_nums) -1

    while a <= b:
        if prime_nums[a] + prime_nums[b] < taget:
            a += 1
        elif prime_nums[a] + prime_nums[b] > taget:
            b -= 1
        elif prime_nums[a] + prime_nums[b]: 
            min_prime.append([a, b])
            a += 1
            b -= 1

    print(f"{prime_nums[min_prime[-1][0]]} {prime_nums[min_prime[-1][-1]]}")