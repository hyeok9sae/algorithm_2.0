T = int(input())
for _ in range(T):
    stack = []
    bracket = input()
    for brack in bracket:
        if brack == '(':
            stack.append(brack)
        else:
            if len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(brack)
            else:
                stack.append(brack)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')