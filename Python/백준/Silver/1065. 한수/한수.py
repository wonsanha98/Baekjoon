def hansu(s :list):
    if len(s) == 1:
        return True

    sus = []
    for i in range(2):
        sus.append(s[i] - s[i+1])

    if sus[0] != sus[1]:
        return False
    else:
        return True
    
def spl(n):
    numbers = []
    for i in str(n):
        numbers.append(i)

    count_hansu = list(map(int, numbers))
    return count_hansu
    
number = int(input())

count = 0

for i in range(1, number+1):
    if i < 100:
        count += 1
    else:
        if hansu(spl(i)):
            count += 1

print(count)