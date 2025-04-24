def bubble_sort(a : list) -> list:
    n = len(a)
    k = 0
    while k < n-1:
        last = n-1
        for j in range(n -1, k, -1):
            if a[j - 1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last
    return a

nums = []
N = int(input())
for i in range(N):
    num = int(input())
    nums.append(num)

for i in bubble_sort(nums):
    print(i)