from collections import deque

def is_in(nz, ny, nx):
    if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def bfs():
    deq = deque()
    count = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if matrix[h][i][j] == 1:
                    visited[h][i][j] = True
                    deq.append((h, i, j, count))
    while deq:
        z, y, x, cnt = deq.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if not is_in(nz, ny, nx):
                continue
            if matrix[nz][ny][nx] != 0 or visited[nz][ny][nx]:
                continue
            visited[nz][ny][nx] = True
            matrix[nz][ny][nx] = 1
            deq.append((nz, ny, nx, cnt+1))
    if not chk_tomato():
        return -1
    else:
        return cnt

def chk_tomato():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if matrix[h][i][j] == 0:
                    return False
    return True

M, N, H = map(int, input().split())
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
matrix = []
dz, dy, dx = (0, 0, 0, 0, -1, 1), (0, -1, 0, 1, 0, 0), (-1, 0, 1, 0, 0, 0)
for _ in range(H):
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    matrix.append(lst)
answer = bfs()
print(answer)