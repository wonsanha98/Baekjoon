max = 0
a = 0
for i in range(9):
    num = int(input())
    if num > max:
        max = num
        a = i+1

print(max)
print(a)