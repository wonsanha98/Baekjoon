a = int(input())
b = int(input())
c = int(input())

abc = list(map(int, list(str(a * b * c))))

for i in range(10):
    print(abc.count(i))
