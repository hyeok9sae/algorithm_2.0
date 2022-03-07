T = int(input())
for _ in range(T):
    L = input()
    lst1, lst2 = [], []
    for key in L:
        if key == '<':
            if len(lst1) != 0:
                lst2.append(lst1.pop())
        elif key == '>':
            if len(lst2) != 0:
                lst1.append(lst2.pop())
        elif key == '-':
            if len(lst1) != 0:
                lst1.pop()
        else:
            lst1.append(key)
    lst2.reverse()
    print(*(lst1+lst2), sep="")
