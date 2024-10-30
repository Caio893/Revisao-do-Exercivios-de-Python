n1 = int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')), int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: '))
print(f'Os numeros digitados foram {n1}')
print(f'Os numeros pares são: ',end='')
for n in n1:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print(f'\nO numero 9 aparece {n1.count(9)} vezes')
if 3 in n1:
    print(f'O numero 3 aparece na {n1.index(3) + 1} posição')
else:
    print('O numero 3 não aparece nessa tupla')