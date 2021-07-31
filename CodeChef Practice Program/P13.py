t = int(input())
while t:
    a, b, c, d = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if a == b and c == d:
        print("YES")
    else:
        if a == c and b == d:
            print("YES")
        else:
            if a == d and b == c:
                print("YES")
            else:
                print("NO")
    t -= 1