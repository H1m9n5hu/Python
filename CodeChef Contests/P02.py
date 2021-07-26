t = int(input())
while t:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if a + b < 3:
        print(1)
    else:
        if 3 <= a + b and a + b <= 10:
            print(2)
        else:
            if 11 <= a + b and a + b <= 60:
                print(3)
            else:
                print(4)
    t -= 1