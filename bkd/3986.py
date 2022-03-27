N = int(input())
answer = 0
for _ in range(N):
    stack = []
    string = input()
    for s in string:
        if not stack:
            stack.append(s)
            continue
        if s == 'A':
            if stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(s)
        elif s == 'B':
            if stack[-1] == 'B':
                stack.pop() 
            else:
                stack.append(s)
    if not stack:
        answer += 1
print(answer)