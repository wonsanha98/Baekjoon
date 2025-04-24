num = int(input())
      
      
def nQ(N):
    nqs = []
    pos = [0] * N
    flag_a = [False] * N
    flag_b = [False] * (N + N-1)
    flag_c = [False] * (N + N-1)
    
    def put() -> None:
        for i in range(N):
            nqs.append(pos[i])
    
    def set(i: int) -> None: 
        for j in range(N):
            if(not flag_a[j]
               and not flag_b[i+j]
               and not flag_c[i-j +(N-1)]):
               pos[i] = j
               if i == N-1:
                  put()
               else:
                   flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = True
                   set(i+1)
                   flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = False
        
    set(0)

    return len(nqs)//N

print(f"{nQ(num)}")