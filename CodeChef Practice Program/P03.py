t = int(input())
while t:

    N = int(input())

    if N == 1:
        print("no")
    else:
        for i in range(2, N + 1):
            if i == N:
                print("yes")
            else:
                if N%i == 0:
                    print("no")
                    break
    t -= 1
