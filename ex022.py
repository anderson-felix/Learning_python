name = str(input('Digite seu nome completo : ')).strip()
ma = name.upper()
mi = name.lower()
tl = name.split()
pn = name.split()
print("""
    Todas letras maiúsculas........ : {}
    Todas letras minúsculas........ : {}
    Quantas letras (exceto espaços) : {}
    Quantas letras no primeiro nome : {}
    """.format(ma, mi, len(''.join(tl)), len(pn[0])))