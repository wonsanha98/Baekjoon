import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, height, visited, ground, n):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and  0 <= ny < n:
            if not visited[nx][ny] and ground[nx][ny] > height:
                dfs(nx, ny, height, visited, ground, n)

n = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

max_heigt = max(map(max, ground))

max_safe_zone = 1

for h in range(1, max_heigt + 1):
    visited = [[False] * n for i in range(n)]
    safe_zone_count = 0

    for i in range(n):
        for j in range(n):
            if ground[i][j] > h and not visited[i][j]:
                dfs(i, j, h, visited, ground, n)
                safe_zone_count += 1
        
    max_safe_zone = max(max_safe_zone, safe_zone_count)

print(max_safe_zone)