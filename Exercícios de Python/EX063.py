print(f'Desafio 63'.center(64, '@'))
termos = int(input('Qual o primeiro termos\n ->'))
c = 0
ultimo = 0
penultimo =1
if termos == 1 or termos == 2:
    print(f'O valor é 1')
else:
    while c <= termos:
        c += 1
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
