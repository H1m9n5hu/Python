def HCF(A, B):
    if B == 0:
        return A
    return HCF ( B, A%B )

def LCM(A, B):
    return ( A / HCF ( A, B ) ) * B

t = int(input())
while t:
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
    
    print(f"{HCF(A, B)} {int(LCM(A, B))}")
    t -= 1