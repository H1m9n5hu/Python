t = int(input())
while t:

    N = int(input())
    string = str(N)
    
    # Using extended slice syntax
    if string == string[::-1]:
        print("wins")
    else:
        print("loses")

    # Using reversed method
    # if string == "".join(reversed(string)):
    #     print("wins")
    # else:
    #     print("loses")

    t -= 1