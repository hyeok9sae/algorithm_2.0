import random
lst = []
for _ in range(9):
    size = int(input())
    lst.append(size)
while True:
    random.shuffle(lst)
    if sum(lst[:7]) == 100:
        answer = lst[:7]
        answer.sort()
        break
print(*answer, sep="\n")