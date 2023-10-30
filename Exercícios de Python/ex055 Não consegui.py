print('---Desafio 56---')
pesado = 0
leve = 0
for c in range(0,5):
    peso = float(input(f'Peso da {c+1} pessoa: '))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            maior = peso
        if peso < leve:
            leve = peso
print(f'o fdp {pesado}')
print(f'o fdp {leve}')