while True:
    stack = []
    string = input()
    if string[0] == '.':
        break
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack:
                stack.append('.')
                break
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                break
        elif s == ']':
            if not stack:
                stack.append('.')
                break
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                break
    if not stack:
        print("yes")
    else:
        print("no")