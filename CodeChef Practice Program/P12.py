t = int(input())
while t:
    X = int(input())
    turns = 0
    if X%5 == 0:
        while X%10 != 0:
            X *= 2
            turns += 1
        print(turns)
    else:
        print(-1)
    t -= 1