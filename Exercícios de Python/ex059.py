n1 = int(input('Digite um termo: '))
menos = n1
inicial = n1
fim = False
resultado = 0
print()
while not fim:
    if menos >= 0:
        menos -= 1
        novo_n1 = n1 * menos
        n1 = novo_n1
        print(f'Calculando {inicial}! = {inicial} x {menos} = {resultado}')
    else:
        fim = True
    resultado = n1
