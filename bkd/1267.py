N = int(input())
lst = list(map(int, input().split()))
Y, M = 0, 0
for i in lst:
    Y += 10+i//30*10
for i in lst:
    M += 15+i//60*15
if Y < M:
    print("Y", Y, sep=" ")
elif Y == M:
    print("Y M", Y, sep=" ")
else:
    print("M", M, sep=" ")