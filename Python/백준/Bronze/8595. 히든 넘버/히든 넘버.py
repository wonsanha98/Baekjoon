import sys
input = sys.stdin.readline

length = int(input())
hidden_number = input()

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0

temp = ['0']

for i in hidden_number:
    if i in number:
        temp.append(i)
    else:
        sum += int(''.join(temp))
        temp = ['0']

print(sum)