num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m0 Número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('ELE É PRIMO!!')
else:
    print('ELE NÃO É PRIMO')
    
'''print('---Desafio 52---') #Eu consegui fazer o objetivo mas não igual ao do professor.
numero = int(input('Digite um numero para vermos se ele é primo\n-> '))
maior = 0
for c in range(1, numero+1):
    if numero % c == 0 and numero // 1 == numero:
        maior += 1
    if numero % c == 0:
        print('\033[34m', end='')
if maior == 2:
        print(f'{numero} é um numero Primo pois foi dividido {maior} vezes')
else:
    print(f'{numero} Não é um número primo.')''' 