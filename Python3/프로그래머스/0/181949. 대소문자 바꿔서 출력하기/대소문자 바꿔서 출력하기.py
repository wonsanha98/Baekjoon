str = input()
for i in str:
    if i == i.lower():
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')
