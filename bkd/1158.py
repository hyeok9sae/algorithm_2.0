N, K = map(int, input().split())
lst = [i for i in range(1, N+1)] + [1]
start = 0
answer = []
while len(answer) != N:
    for i in range(K):
        new_start = lst[start]
        if i == K-1:
            answer.append(str(lst[start]))
            lst[start] = lst[new_start]
            break
        start = new_start
print('<'+', '.join(answer)+'>')