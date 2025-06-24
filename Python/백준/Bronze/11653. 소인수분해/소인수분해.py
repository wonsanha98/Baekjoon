import math

N = int(input())  
d = 2               
sqrt = int(math.sqrt(N)) 

while d <= sqrt:
    if N % d != 0:  
        d += 1      
    else:           
        print(d)    
        N //= d     

if N > 1:
    print(N)