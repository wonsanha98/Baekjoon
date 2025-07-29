import sys
input = sys.stdin.readline

N_str = input()
N_len = len(N_str)      # N의 자리수
N_int = int(N_str)         
max = (N_len * 9)
min_maker = 0

for i in range(max + 1): # 자리수의 최대합
    sum = 0
    new_N = N_int - i
    if new_N < 0:
        continue
    
    new_N = str(N_int - i)

    for j in range(len(new_N)):
        sum += int(new_N[j])
    
    if int(new_N) + sum == N_int:
        min_maker = int(new_N)

print(min_maker)