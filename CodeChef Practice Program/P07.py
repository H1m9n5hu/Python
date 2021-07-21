t = int(input())
while t:
    B = int(input())
    if B%2 == 0:
        T = B*B/2
        S = T - B
    else:
        B -= 1 
        T = B*B/2
        S = T - B 
    print(int(S/4))
    t -= 1