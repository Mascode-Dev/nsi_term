def nombre_de_bits(n):
    binaire=bin(n)[2:]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return nombre_de_bits(n-1)

print(nombre_de_bits(255))