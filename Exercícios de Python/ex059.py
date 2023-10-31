print(f'Desafio 59'.center(16, '*'))
num1 = int(input('Digite o Primeiro valor\n ->'))
num2 = int(input('Digite o Segundo valor\n ->'))
option = 9
      
while option != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    option = int(input('\n->'))
    if option == 1:
        soma = num1 + num2
        print(f'A soma entre {num1}+{num2} é de {soma}')
    
    if option == 2:
        multiplicar = num1 * num2
        print(f'A Multiplicação de {num1}x{num2} é de {multiplicar}')
    
    if option == 3:
        maior = num1
        if num2 > num1:
            maior = num2
            print(f'O maior número entre {num1} e {num2} é {maior}')
        elif maior == num2:
            print('Não tem maior os dois valores são iguais')
    
    if option == 4:
        num1 = int(input('Digite novos valores\n-> '))
        num2 = int(input('Digite novos valores\n-> '))
    
    if option == 5:
        print('Obrigado')
    
    if option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        print('Opção invalida tente novamente entre 1 e 5')
    
    