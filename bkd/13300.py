N, K = map(int, input().split())
lst = [[0]*6 for _ in range(2)]
for _ in range(N):
    S, Y = map(int, input().split())
    lst[S][Y-1] += 1
answer = 0
for i in lst:
    for n in i:
        if n != 0:
            answer += n//K+n%K
print(answer)    