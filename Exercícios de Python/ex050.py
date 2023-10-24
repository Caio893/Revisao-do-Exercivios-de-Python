resultado = 0
total = 0
print('---Desagio 50---')
for c in range(1, 7):
    par = int(input(f'Digite os {c} números\n-> '))
    if par % 2 == 0:
        resultado += par
        total += +1
print(f'Você me informou {total} pares e o soma foi {resultado}')
