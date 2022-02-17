for _ in range(3):
    a, b, c, d = map(int, input().split())
    sum = a+b+c+d
    if sum == 3:
        print('A')
    elif sum == 2:
        print('B')
    elif sum == 1:
        print('C')
    elif sum == 0:
        print('D')
    elif sum == 4:
        print('E')