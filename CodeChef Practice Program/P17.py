t = int(input())
while t:
    N, K = input().split(" ")
    N = int(N)
    K = int(K)
    mutation_like_wolverine = 0
    lst = list(map(int,input().split()))
    for i in range(N):
        value = lst[i] + K
        if value%7 == 0:
            mutation_like_wolverine += 1 
    print(mutation_like_wolverine)
    t -= 1