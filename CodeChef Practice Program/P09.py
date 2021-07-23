t = int(input())
while t:
    N = int(input())
    lst = [0]*N

    for i in range(N):
        lst[i] = list(map(int,input().split()))

    for i in range(N-2, -1, -1):
	    for j in range(0, i + 1):
	        lst [i][j] += max ( lst[i+1][j], lst [i+1][j+1] )
	
    print(lst[0][0])

    t -= 1