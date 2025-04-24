c = int(input())

for i in range(c):
    nums = list(map(int, input().split()))
    n = nums[0]
    scores = nums[1:]

    avg = sum(scores) / n
    count = sum(1 for score in scores if score > avg)

    print(f"{(count / n) * 100: .3f}%")