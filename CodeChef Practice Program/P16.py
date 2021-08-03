N = int(input())
string = str(N)
no_of_digits = len(string)
if no_of_digits == 1:
    print(1)
else:
    if no_of_digits == 2:
        print(2)
    else:
        if no_of_digits == 3:
            print(3)
        else:
            print("More than 3 digits")