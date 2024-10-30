from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram : ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

'''from random import randint
maior = 0
menor = 99999
numero1 = randint(0, 19)
numero2 = randint(0, 19)
numero3 = randint(0, 19)
numero4 = randint(0, 19)
numero5 = randint(0, 19)
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print(tupla[numero1], tupla[numero2], tupla[numero3], tupla[numero4], tupla[numero5])
if numero1 > maior:
    maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
if numero4 > maior:
    maior = numero4
if numero5 > menor:
    menor = numero5
if numero1 < menor:
    menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
if numero4 < menor:
    menor = numero4
if numero5 < menor:
    menor = numero5
print(f'O maior numero é {maior+1}')
print(f'O menor numero é {menor+1}')'''