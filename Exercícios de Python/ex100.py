from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')



numeros = list()
sorteia(numeros)
somaPar(numeros)

'''from random import randint
from time import sleep
numeros = list()
def sorteia():
    n = 0
    print(f'Sorteando números: ', end='')
    for c in range(5):
        sleep(0.3)
        n = randint(1, 10)
        numeros.append(n)
        print(end=' 'f'{n}')
    print(' FIM !')
def somaPAR():
    total = 0
    for v, k in enumerate(numeros):
        if k % 2 == 0:
            total += k
    print(f'Somando os valores pares de {numeros}, temos {total}')


sorteia()

somaPAR()'''