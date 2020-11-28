dia = int(input('Por quantos dias o carro ficou alugado ?\n '))
km = float(input('Informe a quantidade de kilômetros rodados :\n '))
vdia = dia * 60
vkm = km * 0.15
print('Valor total das diárias : R${:.2f}\nValor  da  kilometragem : R${:.2f}\
    nValor  total  a  pagar  : R${:.2f}'.format(vdia,vkm,vdia+vkm))
