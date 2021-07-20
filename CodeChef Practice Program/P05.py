def add(N):
    result = 0
    for i in range(1, N + 1):
        result += i
    return result

def sum(D, N):
    for i in range(1, D + 1):
        N = add(N)
    return N

t = int(input())
while t:

    D, N = input().split(" ")
    D = int(D)
    N = int(N)

    res = sum(D, N)
    print(res)

    t -= 1