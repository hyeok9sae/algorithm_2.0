lst = []
for i in range(1, 10):
    number = int(input())
    lst.append((number, i))
lst.sort(reverse=True)
print(*lst[0], sep="\n") 