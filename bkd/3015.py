N = int(input())
stack = []
answer = 0
for _ in range(N):
    tall = int(input())
    count = 1
    while stack and stack[-1][0] < tall:
        answer += stack.pop()[1]
    if stack and stack[-1][0] == tall:
        count = stack.pop()[1]
        answer += count
        count += 1
        if stack:
            answer += 1
        stack.append((tall, count))
    else:
        if stack:
            answer += 1
        stack.append((tall, 1))
print(answer)