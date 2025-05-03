import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, cnt):
    visited[start] = True
    result[start] = cnt

    for i in sorted(graph[start], reverse=True):
        if not visited[i]:
            dfs(i, cnt+1)

n, m, r = map(int, input().split())
visited = [False] * (n+1)
result = [-1] * (n+1)

graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

dfs(r, cnt)

for i in range(1, n+1):
    print(result[i])