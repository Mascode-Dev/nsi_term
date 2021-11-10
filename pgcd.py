def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b #Reste de la division de a par b
        return pgcd(b,r) # -> b=rq+r'

