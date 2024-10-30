maior = 0
menor = 0
for c in range(0, 6):
    peso = (int(input('Peso: ')))
    if c == 1: # No laço c == 1 o primeiro peso vai ser o maior e menor peso. E não a variavel peso como um todo
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'maior {maior}')
print(f'menor {menor}')

















'''soma = 0
maior = 0
menor = 10000
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi {maior}KG')
print(f'O menor o menor peso lido foi {menor}KG')'''
