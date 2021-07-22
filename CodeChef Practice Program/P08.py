t = int(input())
while t:
    N = int(input())
    lst = []
    lst = list(map(int,input().split()))
    # You can also do like that...
    # lst = list(map(int,input().strip().split(' ')))[:N]    
    lst.sort()
    print(lst[0] + lst[1])
    t -= 1