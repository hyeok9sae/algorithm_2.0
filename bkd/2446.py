N = int(input())
for i in range(1, 2*N):
    if i <= N:
        print(" "*(i-1)+"*"*(2*(N-(i-1))-1))
    else:
        print(" "*(2*N-i-1)+"*"*(2*(i-N)+1))