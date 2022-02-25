S = input()
lst = [0]*26
for s in S:
    lst[ord(s)-97] += 1
print(*lst)