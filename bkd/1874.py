n = int(input())
number = 0
stack = []
num_lst = [i for i in range(n, 0, -1)]
flag = False
answer = []
for _ in range(n):
    target = int(input())
    if number < target:
        while True:
            if not num_lst:
                flag = True
                break
            stack.append(num_lst.pop())
            answer.append('+')
            if stack[-1] == target:
                number = target
                stack.pop()
                answer.append('-')
                break
    else:
        while True:
            if not stack:
                flag = True
                break
            num = stack.pop()
            answer.append('-')
            if num == target:
                number = target
                break
    if flag:
        answer = ['NO']
        break
print(*answer, sep="\n")