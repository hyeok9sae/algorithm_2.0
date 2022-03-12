import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
stack = []
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            print(str(stack.pop())+'\n')
        else:
            print('-1'+'\n')
    elif cmd[0] == 'size':
        print(str(len(stack))+'\n')
    elif cmd[0] == 'empty':
        if not stack:
            print('1'+'\n')
        else:
            print('0'+'\n')
    elif cmd[0] == 'top':
        if stack:
            print(str(stack[-1])+'\n')
        else:
            print('-1'+'\n')