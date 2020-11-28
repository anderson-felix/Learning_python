num = int(input('Digite um número de 0 a 9999 : '))
n = str(num).zfill(4)
print("""
    Unidade : {}
    Dezena  : {}
    Centena : {}
    Milhar  : {}
""".format(n[3],n[2],n[1],n[0]))