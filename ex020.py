from random import SystemRandom
random = SystemRandom()
lista = []
i,n = 0,0
qtd = int(input('Informe a quantidade de alunos na sala : '))
while i < qtd:
    a = str(input('Digite o nome do {:2}° aluno : '.format(i+1)))
    lista.append(a)
    i+=1
random.shuffle(lista)
print('\nA lista sorteada foi :')
while n < qtd:
    print('{:2}° aluno escolhido : {}'.format(n+1,lista[n]))
    n+=1


