from collections import deque

def is_in(x):
    if 0 <= x <= 100000:
        return True
    return False

def bfs(n):
    visited[n] = True
    deq = deque()
    count = 0
    deq.append((n, count))
    while deq:
        X, cnt = deq.popleft()
        if X == K:
            return cnt
        for i in range(3):
            if i == 0:
                nX = X - 1
            elif i == 1:
                nX = X + 1
            else:
                nX = 2 * X
            if not is_in(nX) or visited[nX]:
                continue
            visited[nX] = True
            deq.append((nX, cnt+1))

N, K = map(int, input().split())
visited = [False]*100001
answer = bfs(N)
print(answer)