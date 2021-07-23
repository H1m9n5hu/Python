t = int(input())
while t:
    lst = list(map(int,input().split()))
    N = lst.pop(0)
    minimum_value = min(lst)
    
    for i in range(1, minimum_value + 1):
        for j in range(N):
            if lst[j]%i != 0:
                break
            if j == N - 1 and lst[N-1]%i == 0:
                r = i
    
    for i in range(N):
        print(int(lst[i]/r),end=" ")
    
    t -= 1