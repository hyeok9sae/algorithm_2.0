from collections import deque

def chk_ripe():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                return False
    return True

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def bfs(lst):
    deq = deque()
    for row, col in lst:
        visited[row][col] = True
        deq.append((row, col, 0))
    while deq:
        y, x, count = deq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == -1:
                continue
            if matrix[ny][nx] != 0 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            matrix[ny][nx] = 1
            deq.append((ny, nx, count+1))
    return count

M, N = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
visited = [[False]*M for _ in range(N)]
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
lst = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            lst.append((i, j))
answer = bfs(lst)
print(*matrix, sep="\n")
if chk_ripe():
    print(answer)
else:
    print(-1)