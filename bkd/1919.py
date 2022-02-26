string1, string2 = input(), input()
lst1, lst2 = [0]*26, [0]*26
for s1 in string1:
    lst1[ord(s1)-97] += 1
for s2 in string2:
    lst2[ord(s2)-97] += 1
for i in range(26):
    lst1[i] = abs(lst1[i]-lst2[i])
print(sum(lst1))