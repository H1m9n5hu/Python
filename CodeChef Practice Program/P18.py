######## Bubble Sort ########

lst = []
n = int(input("Enter the size of list : "))
print("Enter the elements of the list : ")
for i in range(n):
    lst.append(int(input()))
counter = 1
while counter < n:
    for i in range(n-counter-1):
        temp = lst[i]
        if lst[i] > lst[i+1]:
            lst[i] = lst[i+1]
            lst[i+1] = temp
    counter += 1
print(lst)
