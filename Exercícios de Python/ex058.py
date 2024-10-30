encerrar = False
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while not encerrar:
    print(f'Escolha a opção: \n[1] Somar\n[2] Multiplicar\n[3] Dividir\n[4] Novos Números\n[5] Encerrar\n')
    option = int(input('Opção: '))
    if option == 5:
        encerrar = True
    else:
        if option == 1:
            soma = n1 + n2
            print(f'A soma de {n1} + {n2} é {soma}')
        elif option == 2:
            multiplicar = n1 * n2
            print(f'A multiplicação de {n1} e {n2} é {multiplicar}')
        elif option == 3:
            dividir = n1 / n2
            print(f'A divisão de {n1} e {n2} é {dividir}')
        elif option == 4:
            novo_n1 = int(input('Digite um novo número: '))
            n1 = novo_n1
            novo_n2 = int(input('Digite um novo número: '))
            n2 = novo_n2
print('Obrigado !')


