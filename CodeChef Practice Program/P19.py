######## Insertion Sort ########

lst = []
n = int(input("Enter the size of list : "))
print("Enter the list elements : ")
for i in range(n):
    lst.append(int(input()))
for i in range(1, n):
    current = lst[i]
    j = i - 1
    while lst[j] > current and j >= 0:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = current
print(lst)
