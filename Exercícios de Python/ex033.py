print('--Desafio 33--')
# Entrada das variaveis
num1 = int(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 1->'))
num2 = int(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 2->'))
num3 = int(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 3->'))

# Vereficando quem é o menor
maior = num1
menor = num2

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3
print(f'O maior númeor é o {maior}')
print(f'O menor númeor é o {menor}')