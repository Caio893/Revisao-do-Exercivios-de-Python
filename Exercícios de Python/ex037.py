"""print('---Desafio 37---')
numero = int(input('Digite um numero que você deseja fazer a conversão\n->'))
escolha = int(input('1 para binário\n2 para Octal\n3 para Hexdecimal\n4 para todos os valores\n->'))
if escolha == 1:
    binario = bin(numero)[2:]
    print(f'O Numero {numero} convertido em Binario é {binario}')
elif escolha == 2:
    oct = oct(numero)[2:]
    print(f'O Número {numero} convertido em Octadecimal é {oct}')
elif escolha == 3:
    hex = hex(numero)[2:]
    print(f'O Número {numero} convertido em Hexadecimal é {hex}')
elif escolha == 4:
    binario = bin(numero)[2:]
    oct = oct(numero)[2:]
    hex = hex(numero)[2:]
    print(f'O Número {numero} convertido em todas as possibilidaes é \n{binario} Binário\n{oct} Octadecimal\n{hex} Hexadecimal')
else:
    print(f'Erro porfavor tente novamente digitando um numero de 1 a 4.')
"""
def converter_base(numero, base):
    if base == 1:
        return bin(numero)[2:]
    elif base == 2:
        return oct(numero)[2:]
    elif base == 3:
        return hex(numero)[2:]
    else:
        raise ValueError("Base de conversão inválida")

def main():
    print('---Desafio 37 (Avançado)---')
    try:
        numero = int(input('Digite um número que você deseja converter: '))
        escolha = int(input('Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\n4 para todas as opções\n->'))

        if escolha == 4:
            for base in range(1, 4):
                resultado = converter_base(numero, base)
                print(f'O número {numero} convertido em base {base} é {resultado}')
        elif escolha in [1, 2, 3]:
            resultado = converter_base(numero, escolha)
            print(f'O número {numero} convertido em base {escolha} é {resultado}')
        else:
            print('Escolha inválida. Por favor, selecione uma opção de 1 a 4.')

    except ValueError as ve:
        print(f"Erro: {ve}")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

if __name__ == "__main__":
    main()
