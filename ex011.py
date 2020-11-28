l = float(input('Informe a LARGURA da parede : '))
a = float(input('Informe a ALTURA da parede  : '))
area = l*a
print('\nSua parede de {} x {} tem a área de {:.2f} M² \nPara pintar você vai precisar de {:.1f} litros de tinta.'.format(l,a,area,area/2))