lst = []
for _ in range(7):
    number = int(input())
    if number%2 != 0:
        lst.append(number)
lst.sort()
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst), min(lst), sep="\n")
