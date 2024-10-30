from random import randint
from time import sleep
total = int(input('Quantos jogos você quer que eu sorteie: '))
valores = []
lista_total = []
print(f'SORTEANDO 10 JOGOS')

for c in range(total):
    while True:
        n = randint(1, 60)
        if n not in valores:
            valores.append(n)
        if len(valores) == 6:
            lista_total.append(valores[:])
            break
    valores.sort()
    print(f'Jogo {c+1}: {valores}')
    valores.clear()
print(lista_total)