import sys

def permutation(arr, r):
    result = []

    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return
        
        for idx, data in enumerate(arr):
            if idx not in index:
                permute(p + [data], index + [idx])
    
    permute([], [])

    return result

def su(arr, i):
    haparr = []
    while i > 0:
        if (arr[i] - arr[i-1]) < 0:
            haparr.append((arr[i] - arr[i-1])*-1)
        else:
            haparr.append(arr[i] - arr[i-1])
        i -= 1
    return sum(haparr)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
hap = []

for li in permutation(nums, len(nums)):
    hap.append(su(li, len(li)-1))

hap.sort()

print(hap[-1])