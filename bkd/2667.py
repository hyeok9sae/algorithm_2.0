from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    count = 0
    while deq:
        y, x = deq.popleft()
        count += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != 1 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
    return count

N = int(input())
matrix = []
visited = [[False]*N for _ in range(N)]
ans_count = 0
ans_lst = []
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
for _ in range(N):
    matrix.append(list(map(int, input())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            ans_lst.append(bfs(i, j))
            ans_count += 1
ans_lst.sort()
print(ans_count)
print(*ans_lst, sep="\n")