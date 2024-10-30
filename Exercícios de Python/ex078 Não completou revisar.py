numero = []
maior = 0
menor = 0
for n in range(0, 5):
    numero.append(int(input(f'Digite um valor para a Posição {n}: ')))
    if n == 1:
        maior = menor = numero[n]
    else:
        if maior < numero[n]:
            maior = numero[n]
        if menor > numero[n]:
            menor = numero[n]
print(f'Você digitou os valores {numero}')
print(f'O maior é {maior} e está na posição',end='')
for v, i in enumerate(numero):
    if i == maior:
        print(f' {v}...', end='')
print(f'\nO menor é {menor} e está na posição', end='')
for v, i in enumerate(numero):
    if i == menor:
        print(f' {v}...',end='')