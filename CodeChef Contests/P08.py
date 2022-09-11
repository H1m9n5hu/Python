t = int(input())
while t:
    a, x, b, y = input().split(" ")
    if int(a)/int(x) > int(b)/int(y):
        print("Alice\n")
    elif int(a)/int(x) < int(b)/int(y):
        print("Bob\n")
    else:
        print("Equal\n")
    t -= 1