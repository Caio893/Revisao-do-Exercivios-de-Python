'''""print('---Desafio 38---')
numero1 = int(input('Primeiro valor:\n->'))
numero2 = int(input('Segundo valor:\n->'))

if numero1 > numero2:
    print(f'O Primeiro valor {numero1} é o maior')
elif numero1 < numero2:
    print(f'O Segundo valor {numero2} é o maior')
else:
    print(f'O dois valores são iguais')
""'''
def comparar_numeros():
    try:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))

        if numero1 > numero2:
            resultado = f'O primeiro valor {numero1} é maior.'
        elif numero1 < numero2:
            resultado = f'O segundo valor {numero2} é maior.'
        else:
            resultado = 'Não existe valor maior, os dois são iguais.'

        return resultado

    except ValueError:
        return 'Erro: Digite números inteiros válidos.'
    except KeyboardInterrupt:
        return 'Programa encerrado pelo usuário.'

def main():
    print('---Desafio 38 (Avançado)---')
    resultado = comparar_numeros()
    print(resultado)

if __name__ == "__main__":
    main()
