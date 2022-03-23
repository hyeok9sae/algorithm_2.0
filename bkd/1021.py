from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
deq = deque(i for i in range(1, N+1))
for i in lst:
    if i == deq[0]:
        deq.popleft()
    else:
        if deq.index(i) <= len(deq)//2:
            while i != deq[0]:
                deq.append(deq.popleft())
                answer += 1
            deq.popleft()
        else:
            while i != deq[0]:
                deq.appendleft(deq.pop())
                answer += 1
            deq.popleft()
print(answer)