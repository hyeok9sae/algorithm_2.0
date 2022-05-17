from collections import deque

def is_in(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] <= height or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))

N = int(input())
matrix = []
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
for i in range(N):
    matrix.append(list(map(int, input().split())))
height = 1
max_res = 1
while height <= 100:
    count = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > height and not visited[i][j]:
                bfs(i, j)
                count += 1
    if max_res < count:
        max_res = count
    height += 1
print(max_res)