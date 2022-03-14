N = int(input())
A = list(map(int, input().split()))
stack = []
answer = [-1]*len(A)
for idx, i in enumerate(A):
    if not stack:
        stack.append((i, idx))
    else:
        while stack:
            if stack[-1][0] < i:
                num, num_idx = stack.pop()
                answer[num_idx] = i
                if not stack:
                    stack.append((i, idx))
                    break
            else:
                stack.append((i, idx))
                break
print(*answer)