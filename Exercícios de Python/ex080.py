lista = []
for c in range(0, 5):
    n = int(input('Digite o numero: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista....')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Foi adicionado na posição {pos} da lista....')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
'''valores = list()
menor = maior = 0
for c in range(5):
    n = input('Digite um numero: ')
    if c == 0:
        menor = maior = n
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        if n >= maior:
            maior = n
            valores.append(n)
            print('Adicionado ao final da lista...')
        if n <= menor:
            menor = n
            valores.insert(0,n)
            print(f'Foi adicionado no índice {0}')
    if maior > n > menor:
        for _, i in enumerate(valores):
            if n < i:
                valores.insert(_,n)
                print(f'Foi adicionado no índice {_}')
                break

print(f'Os valores digitados em ordem foram {valores}')'''