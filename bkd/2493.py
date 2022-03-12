N = int(input())
tower = list(map(int, input().split()))
stack = [(tower[0], 0)]
answer = [0]
laser = 0
for idx, t in enumerate(tower[1:]):
    while True:
        if stack[-1][0] < t:
            stack.pop()
            if not stack:
                stack.append((t, idx+1))
                answer.append(0)
                break
        else:
            answer.append(stack[-1][1]+1)
            stack.append((t, idx+1))
            break
print(*answer)