from time import sleep

def maior(*num):
    cont=maior=0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2,4,7,8,9,4)
maior(8,9,7,5,56)
maior()
maior(6)

'''from time import sleep
def maior_valor(*n):
    maior = 0
    valores = list()
    print('-='*50)
    print(f'Analisando os valores passados...')
    for v, k in enumerate(n):
        valores.append(k)
    for v, k in enumerate(valores):
        if v == 0:
            maior = k
        else:
            if k > maior:
                maior = k
    for c in valores:
        sleep(0.3)
        print(f'{c}', end=' ')
    sleep(1)
    print(f'\nForam informados {len(valores)} valores ao todo.')
    print(f'O maior valor encontrado foi {maior}')

maior_valor(5)
maior_valor(4,5,8,7)
maior_valor(9,7,8)
maior_valor(8,57,9)
maior_valor(0)'''