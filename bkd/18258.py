import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deq = deque()
for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        deq.append(cmd[1])
    elif cmd[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)