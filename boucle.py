def boucle(k,n):
    if k==n:
        return n
    else:
        print(k)
        return boucle(k+1,n)

print(boucle(2,8))