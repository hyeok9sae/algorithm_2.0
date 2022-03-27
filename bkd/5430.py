from collections import deque

T = int(input())
for _ in range(T):
    flag = False
    chk = False
    p = input()
    n = int(input())
    x = input()
    if x == '[]':
        deq = deque()
    else:
        deq = deque(x[1:-1].split(","))
    for i in p:
        if i == 'R':
            if not flag:
                flag = True
            else:
                flag = False
        elif i == 'D':
            if not deq:
                chk = True
                break
            if not flag:
                deq.popleft()
            else:
                deq.pop()
    if chk:
        print("error")
    else:
        if not flag:
            lst = list(deq)
            print("["+','.join(lst)+"]")
        else:
            lst = list(deq)[::-1]
            print("["+','.join(lst)+"]")