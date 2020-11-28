from math import sqrt, hypot

a = float(input('Informe o valor do cateto ADJACENTE : '))
o = float(input('Informe o valor do cateto OPOSTO : '))

h = sqrt((a**2) + (o**2)) # OU h = (((a**2) + (o**2)) ** (1/2))

#h = hypot(a,o)

print('HIPOTENUSA = {:.2f}'.format(h))