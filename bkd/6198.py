N = int(input())
stack = []
answer = 0
for _ in range(N):
    height = int(input())
    if not stack:
        stack.append(height)
    else:
        while True:
            if stack and stack[-1] <= height:
                stack.pop()
            else:
                stack.append(height)
                break
    answer += len(stack)-1
print(answer)