v = float(input('Informe o preço do produto : R$'))
d = float(input('\nInforme a porcentagem do desconto a ser aplicada : '))
des = d/100
print('O preço do produto com {}% de desconto é : {:.2f} R$'.format(d, v-(des*v)))