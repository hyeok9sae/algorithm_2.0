A, B = map(int, input().split())
if A <= B:
    mA, mB = A, B
else:
    mA, mB = B, A 
count = mB-mA-1
if count <= 0:
    print(0)
else:
    print(count)
for i in range(mA+1, mB):
    print(i, end=" ")