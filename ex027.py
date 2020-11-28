n = input('Digite um nome completo : ')
pn = n.split()
print(f"""\n
    Nome completo : {n}
    Primeiro nome : {pn[0]}
    Último nome   : {pn[-1]}
""")