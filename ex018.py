from math import sin, cos, tan, radians

ang = float(input('Informe o valor do ÂNGULO : '))

a = radians(ang)

s = sin(a)
c = cos(a)
t = tan(a)

print('O ângulo {:.2f} tem :\nSENO : {:.2f}\nCOSSENO : {:.2f}\nTANGENTE : {:.2f}'.format(a,s,c,t))
