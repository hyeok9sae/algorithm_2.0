from collections import deque

def is_in(hei, row, col):
    if 0 <= hei < L and 0 <= row < R and 0 <= col < C:
        return True
    return False

def bfs(hei, row, col):
    visited[hei][row][col] = True
    deq = deque()
    deq.append((hei, row, col, 0))
    while deq:
        z, y, x, count = deq.popleft()
        if matrix[z][y][x] == 'E':
            return count
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if not is_in(nz, ny, nx):
                continue
            if matrix[nz][ny][nx] == '#' or visited[nz][ny][nx]:
                continue
            visited[nz][ny][nx] = True
            deq.append((nz, ny, nx, count+1))
    return -1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    matrix = []
    for _ in range(L):
        lst = []
        for _ in range(R):
            lst.append(list(input()))
        matrix.append(lst)
        input()
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    dz, dy, dx = (1, -1, 0, 0, 0, 0), (0, 0, 0, -1, 0, 1), (0, 0, -1, 0, 1, 0)
    flag = False
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if matrix[i][j][k] == 'S':
                    res = bfs(i, j, k)
                    if res != -1:
                        print("Escaped in " + str(res) + " minute(s).")
                    else:
                        print("Trapped!")
                    flag = True
                    break
            if flag:
                break
        if flag:
            break