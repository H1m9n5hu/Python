import math
t = int(input())
while t:
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
    if A == B:
        X = A
    else:
        X = A + 1
    sum = math.ceil ( (B - X)*1.0/2 ) + math.ceil ( (X - A)*1.0/2 )
    print(sum)
    t -= 1