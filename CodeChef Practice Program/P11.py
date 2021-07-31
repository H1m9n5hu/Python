t = int(input())
while t:
    N, K = input().split(" ")
    N = int(N)
    K = int(K)
    coins = 0
    for i in range(1, K + 1):
        if N%i > coins:
            coins = N%i
    print(coins)
    t -= 1
