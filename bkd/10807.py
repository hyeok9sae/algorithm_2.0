N = int(input())
lst = list(map(int, input().split()))
v = int(input())
answer = 0
for i in lst:
    if v == i:
        answer += 1
print(answer)