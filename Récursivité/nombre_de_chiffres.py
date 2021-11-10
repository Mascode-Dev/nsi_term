def nombre_de_chiffres(n):
    if n<10:
        return 1
    else:
        return 1+nombre_de_chiffres(n/10)

print(nombre_de_chiffres(21003))