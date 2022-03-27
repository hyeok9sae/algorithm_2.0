from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def bfs():
    visited[0][0] = True
    deq = deque()
    deq.append((0, 0, 1))
    while deq:
        y, x, count = deq.popleft()
        if y == N-1 and x == M-1:
            return count
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != 1 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx, count+1))

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in input()])
visited = [[False]*M for _ in range(N)]
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
answer = bfs()
print(answer)