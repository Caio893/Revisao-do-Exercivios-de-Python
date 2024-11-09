def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabbou de digitar o número {n}')


'''def leiaInt(num):
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('ERRO ! DIGITE UM NÚMEOR VALIDO!')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''