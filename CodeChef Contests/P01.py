t = int(input())
while t:
    N, K = input().split(" ")
    N = int(N)
    K = int(K)
    L = 2**N
    if K < L/2:
        max_val_of_array = (L-1)*K*2
    else:
        max_val_of_array = (L-1)*L
    print(max_val_of_array)
    t -= 1