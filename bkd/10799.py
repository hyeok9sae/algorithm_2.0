bracket = list(input())
answer = 0
stack = []
for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if bracket[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1
print(answer)