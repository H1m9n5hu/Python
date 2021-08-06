t = int(input())
while t:
    a, b, c, d = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if (a != b and c != d) or (a != c and b != d) or (a != d and b != c):
        print(2)
    else:
        if a == b == c == d:
            print(0)
        else:
            print(1)
    t -= 1