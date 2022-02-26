N = input()
lst = [0]*10
flag = False
for num in N:
    if num == '6' or num == '9':
        if not flag:
            lst[6] += 1
            flag = True
        else:
            lst[9] += 1
            flag = False
    else:
        lst[int(num)] += 1
print(max(lst))