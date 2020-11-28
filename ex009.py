n = int(input("Digite um número inteiro : "))
a = 1
print('\t TABUADA \n')
while a <= 10:
    print('{} * {:2} = {}'.format(n,a,n*a)) # O parâmetro {:2} indica que toda impressão terá duas casas.
    a+=1
