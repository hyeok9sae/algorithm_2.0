str1 = list(input())
str2 = []
M = int(input())
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == 'L' and len(str1) != 0:
        str2.append(str1.pop())
    elif cmd[0] == 'D' and len(str2) != 0:
        str1.append(str2.pop())
    elif cmd[0] == 'B' and len(str1) != 0:
        str1.pop()
    elif cmd[0] == 'P':
        str1.append(cmd[1])
str2.reverse()
print(*(str1+str2), sep="")