import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(str(A+B)+"\n")