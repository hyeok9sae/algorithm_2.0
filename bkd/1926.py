from collections import deque

def is_in(ny, nx):
    if 0 <= ny < n and 0 <= nx < m:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    size = 0
    while deq:
        y, x = deq.popleft()
        size += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != 1 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
    return size

n, m = map(int, input().split())
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
visited = [[False]*m for _ in range(n)]
matrix = [[*map(int, input().split())] for _ in range(n)]
answer, count = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            result = bfs(i, j)
            count += 1
            if answer < result:
                answer = result
print(count, answer, sep="\n")