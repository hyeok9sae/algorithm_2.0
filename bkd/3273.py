n = int(input())
lst = list(map(int, input().split()))
sum = int(input())
answer = 0
lst.sort()
for i in range(n):
    if lst[i] >= sum:
        break
    for j in range(i+1, n):
        if lst[j] > sum-lst[i]:
            break
        if lst[i]+lst[j] == sum:
            answer += 1
print(answer)  