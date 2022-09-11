t = int(input())
while t:
    w, x, y, z = input().split(" ")
    print(f"{int(w) + (int(x) - int(y))*int(z)}\n")
    t -= 1