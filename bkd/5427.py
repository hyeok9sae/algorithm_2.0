from collections import deque

def is_in(ny, nx):
    if 0 <= ny < M and 0 <= nx < N:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    count = 0
    while deq:
        y, x  = deq.popleft()
        count += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == 1 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
    return count

M, N, K = map(int, input().split())
matrix = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            print(i, j)
            matrix[j][i] = 1
visited = [[False]*N for _ in range(M)]
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
answer = []
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0 and not visited[i][j]:
            result = bfs(i, j)
            answer.append(result)
answer.sort()
print(len(answer))
print(*answer)
