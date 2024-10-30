numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'douze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input(f'Digite um numero entre 0 e 20\nNumero: '))
    if n != int and n < 0 or n > 20:
        print(f'Erro! Tente novamente')
    else:
        break
print(f'Você digitou o Número {numeros[n]}')