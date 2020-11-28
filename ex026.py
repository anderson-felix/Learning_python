f = str(input('Digite um frase : ')).strip()
print("""
    Quantas vezes na frase aparece a letra A  : {}
    Em que posição ela aparece a primeira vez : {}
    Em que posição ela aparece a última vez   : {}
""".format(f.lower().count('a'), f.lower().find('a'), f.lower().rfind('a')))