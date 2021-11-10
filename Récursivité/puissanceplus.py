def puissanceplus(x,n):
    q=n//2
    if n==0:
        return 1
    elif n%2==0:
        p=puissanceplus(x,q)
        return p*p
    elif n%2==1:
        p=puissanceplus(x,q)
        return p*p*x

print(puissanceplus(3,8))