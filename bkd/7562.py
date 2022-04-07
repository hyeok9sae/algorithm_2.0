from collections import deque

def bfs(row, col, e_row, e_col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col, 0))
    while deq:
        y, x, count = deq.popleft()
        if y == e_row and x == e_col:
            return count
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx, count + 1))

def is_in(ny, nx):
    if 0 <= ny < I and 0 <= nx < I:
        return True
    return False

T = int(input())
dy, dx = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, 2, 1, -1, -2)
for _ in range(T):
    I = int(input())
    sY, sX = map(int, input().split())
    eY, eX = map(int, input().split())
    visited = [[False]*I for _ in range(I)]
    answer = bfs(sY, sX, eY, eX)
    print(answer)