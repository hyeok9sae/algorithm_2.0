from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def bfs(row, col, std):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != std or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))

def bfs_rgb(row, col, std):
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            if std == 'R':
                if matrix[ny][nx] != std and matrix[ny][nx] != 'G':
                    continue
            elif std == 'G':
                if matrix[ny][nx] != std and matrix[ny][nx] != 'R':
                    continue
            else:
                if matrix[ny][nx] != std:
                    continue
            visited[ny][nx] = True
            deq.append((ny, nx))

N = int(input())
matrix = []
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
visited = [[False]*N for _ in range(N)]
for _ in range(N):
    matrix.append(list(input()))
answer, answer_rgb = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, matrix[i][j])
            answer += 1
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_rgb(i, j, matrix[i][j])
            answer_rgb += 1
print(answer, answer_rgb)        