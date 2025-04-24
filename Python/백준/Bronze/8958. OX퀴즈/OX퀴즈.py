t = int(input())

for i in range(t):
    sum = 0
    p = 1
    str = list(input())

    for s in str:
        if s == "O":
            sum += p
            p += 1

        else:
            p = 1
    
    print(sum)