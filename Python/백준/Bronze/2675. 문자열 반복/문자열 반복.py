t = int(input())

for i in range(t):
    r, str = input().split()
    r = int(r)
    str = list(str)

    for s in str:
        print(s * r, end="")
        
    print()
