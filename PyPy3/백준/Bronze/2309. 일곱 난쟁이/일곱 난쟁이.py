import sys

nums = []*9

for i in range(9):
    num = int(sys.stdin.readline())
    nums.append(num)

total = sum(nums)
litte = []

for i in range(len(nums)-1):
    j = i +1
    while j < len(nums):
        if total - nums[i] - nums[j] == 100:
            del nums[j] 
            del nums[i]
            break
    
        j += 1
    if len(nums) == 7:
        break

nums.sort()

for i in nums:
    print(i)
