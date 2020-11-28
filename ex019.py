from random import SystemRandom
random = SystemRandom()
qtd = int(input('Informe a quantidade de alunos na sala : '))
lista = []
i = 0
while i < qtd:
    a = str(input('Digite o nome do {:2}° aluno : '.format(i+1)))
    lista.append(a)
    i+=1
print('De {} alunos cadastrados, o aluno escolhido foi : {}'.format(len(lista), random.choice(lista)))
