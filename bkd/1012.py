from collections import deque

def is_in(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != 1 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))

T = int(input())
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1
                bfs(i, j)
    print(count)