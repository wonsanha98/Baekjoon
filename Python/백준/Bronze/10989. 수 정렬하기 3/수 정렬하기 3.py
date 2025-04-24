import sys

N = int(sys.stdin.readline())
nums = [0] *10000

for i in range(N):
    num = int(sys.stdin.readline())
    nums[num-1] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            sys.stdout.write(f"{str(i+1)}\n")