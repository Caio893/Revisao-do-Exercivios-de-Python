def area(a,b):
    metro = a * b
    print(f'A área de um terrono {a}x{b} é de {metro}m²')


print('Controle de Terrenos')
print('-'*15)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura,comprimento)