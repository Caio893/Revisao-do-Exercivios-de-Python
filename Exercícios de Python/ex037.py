import math
numero = int(input('Digite um numero: '))
print(f'Escolha qual opções você quer para converter\n1 Binário\n2 Octal\n3 Hexadecimal')
option = int(input())
if option == 1:
    numero = bin(numero)
    print(f'{numero}'[2:])
elif option == 2:
    numero = oct(numero)
    print(f'{numero}'[2:])
elif option == 3:
    numero = hex(numero)
    print(f'{numero}'[2:])
