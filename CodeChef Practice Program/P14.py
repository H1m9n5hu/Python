t = int(input())
while t:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    add = x + y
    flag = False
    while True:
        add += 1 
        for i in range(2, add + 1):
            if add%i == 0 and add != i:
                break
            if add == i:
                flag = True
        if flag:
            break
    print(add - x - y)
    t -= 1