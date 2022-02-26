N = int(input())
for _ in range(N):
    lst1 = [0]*26
    lst2 = [0]*26
    string1, string2 = map(str, input().split())
    for i, j in zip(string1, string2):
        lst1[ord(i)-97] += 1
        lst2[ord(j)-97] += 1
    flag = False
    for i in range(26):
        if lst1[i] != lst2[i]:
            print("Impossible")
            flag = True
            break
    if not flag:
        print("Possible")