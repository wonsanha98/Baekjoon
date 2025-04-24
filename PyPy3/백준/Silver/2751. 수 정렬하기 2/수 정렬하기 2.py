import sys

def shell_sort(arr :list) -> list:
    n = len(arr)
    gap = 1

    while gap < n//9:
        gap = gap *3 + 1

    while gap > 0:
        for i in range(gap, n):
            j = i - gap
            tmp = arr[i]
            while j >= 0 and arr[j] >tmp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = tmp
        gap//= 3

    return arr

nums = []
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

for i in shell_sort(nums):
    print(i)
