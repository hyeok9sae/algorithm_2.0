from collections import deque

def is_in(nx):
    if 1 <= nx <= F:
        return True
    return False

def bfs(start):
    visited[start] = True
    deq = deque()
    deq.append((start, 0))
    while deq:
        st, count = deq.popleft()
        if st == G:
            return count
        for i in range(2):
            nx = st + dx[i]
            if not is_in(nx):
                continue
            if visited[nx]:
                continue
            visited[nx] = True
            deq.append((nx, count+1))
    return -1

F, S, G, U, D = map(int, input().split())
dx = (U, -1*D)
visited = [False]*(F+1)
result = bfs(S)
if result == -1:
    print("use the stairs")
else:
    print(result)