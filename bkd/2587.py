lst = []
for _ in range(5):
    number = int(input())
    lst.append(number)
lst.sort()
print(sum(lst)//5, lst[2], sep="\n")