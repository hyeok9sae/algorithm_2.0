N = int(input())
for i in range(1, N*2):
    if i <= N:
        print(" "*(N-i)+"*"*(2*i-1))
    else:
        print(" "*(i-N)+"*"*(2*(2*N-i)-1))