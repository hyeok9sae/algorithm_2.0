lst = list(map(int, input().split()))
dice = set(lst)
if len(dice) == 1:
    print(10000+lst[0]*1000)
elif len(dice) == 2:
    for i in dice:
        if i in lst:
            lst.remove(i)
    print(1000+lst[0]*100)
else:
    print(max(lst)*100)