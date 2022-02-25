number = 1
for _ in range(3):
    number *= int(input())
num = str(number)
num_lst = [0]*10
for n in num:
    num_lst[int(n)] += 1
print(*num_lst, sep="\n")