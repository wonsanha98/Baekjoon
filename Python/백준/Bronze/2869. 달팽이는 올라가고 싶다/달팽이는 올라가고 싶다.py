a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)

if a == v:
    print(1)

elif (v-a) % (a-b) == 0:
    print((v-a) // (a-b) + 1)    

else:
    print((v-a) // (a-b) + 2)