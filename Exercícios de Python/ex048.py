s = 0
contador = 0
for c in range(0, 501,3):
    if c % 2 == 1:
        s += c
        contador += 1
print(f'A soma de todos os {contador} valores  é de {s}', end=' ')
