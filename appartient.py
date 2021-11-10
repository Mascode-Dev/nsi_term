def appartient(v,t,i):
    if i==len(t):
        return False
    elif t[i]==v:
        return True
    else:
        return appartient(t,t,i+1)