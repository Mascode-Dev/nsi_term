def fonction(e):
    N=0
    U=2.5
    while abs(U-3)>=e:
        N=N+1
        U=-U**2+5*U-3
        return(N)

print(fonction())