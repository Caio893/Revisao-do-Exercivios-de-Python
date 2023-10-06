print('Desafio 20')
from random import shuffle
a = str(input('Aluno: '))
b = str(input('Aluno: '))
c = str(input('Aluno: '))
d = str(input('Aluno: '))
##sorteio = f'{a} {b} {c} {d}'.split()
sorteio = [a,b,c,d]
shuffle(sorteio)
print(f'E a ordem de apresentação dos trabalhos vai ser: {sorteio}')
