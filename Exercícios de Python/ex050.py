soma = 0
contador = 0
for c in range(0, 6):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'O total de numeros pares foi de {soma} e forma {contador} numeros pares digitados')