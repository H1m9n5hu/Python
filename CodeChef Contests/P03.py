import math
t = int(input())
while t:
    E, K = input().split(" ")
    E = int(E)
    K = int(K)
    len_of_foodchain = 0
    while E:
        len_of_foodchain += 1
        E = math.floor(E/K)
    print(len_of_foodchain)
    t -= 1