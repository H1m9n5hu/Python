t = int(input())
while t:
    N = int(input())
    add = 0
    height = 0
    for i in range(1, N + 1):
        add += i
        if add > N:
            break
        else:
            height += 1
    print(height)
    t -= 1