lst = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    arr = lst[a:b+1]
    arr.reverse()
    for i in range(len(arr)):
        lst[a+i] = arr[i]
print(*lst[1:])