soma = totcont = 0
while True:
    n1 = int(input('Digite númeors: '))
    if n1 == 999:
        break
    totcont += 1
    soma += n1
print(f'A soma de todos os númeors é {soma} e foram {totcont} digitados.')