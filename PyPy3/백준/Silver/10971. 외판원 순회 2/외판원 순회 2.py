import sys

def traveling(arr, visited, now, n , count, cost, min_cost):
    if count == 0 and arr[now][0]:
        return min(min_cost, cost + arr[now][0])
    
    for i in range(n):
        if not visited[i] and arr[now][i]:
            visited[i] = True
            min_cost = traveling(arr, visited, i, n, count - 1, cost + arr[now][i], min_cost) 
            visited[i] = False
        
    return min_cost

def travel(arr):
    n = len(arr)
    visited = [False]*n
    visited[0] = True
    return traveling(arr, visited, 0, n, n-1, 0, sys.maxsize)

N = int(sys.stdin.readline())
citys = []*N

for i in range(N):
    city = list(map(int, sys.stdin.readline().split()))
    citys.append(city)

print(travel(citys))
