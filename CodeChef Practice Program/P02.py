size = int(input())
lst = []
lst = list(map(int,input().strip().split(' ')))[:size]
even_num = 0
odd_num = 0
for i in range(0,size):
    if lst[i]%2 == 0:
        even_num += 1
    else:
        odd_num += 1
if even_num > odd_num:
    print('READY FOR BATTLE')
else:
    print('NOT READY')