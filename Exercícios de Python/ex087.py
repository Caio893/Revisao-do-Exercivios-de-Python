matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = tot3 = maior = 0
for l in range(3): # Criar a Matriz 3x3
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor {l+1}x{c+1}: '))

for l in range(3): # Somar os pares da Matriz
    for c in matriz[l]:
        if c % 2 == 0:
            par += c

for l in range(3): # Encontrar o Maior numero da segunda linha
    for c in matriz[l]:
        for c2 in matriz[1]:
            if c2 == 0:
                maior = c2
            else:
                if maior < c2:
                    maior = c2

for c in range(3): # A soma da terceira coluna
    for _,i in enumerate(matriz[c]):
        if _ == 2:
            tot3 += i

for l in range(3): # Formatação da Matriz deixar ela bonita no print
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print(f'A Soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {tot3}')
print(f'O maior valor da segunda linha é {maior}')