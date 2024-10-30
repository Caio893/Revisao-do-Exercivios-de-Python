numero = int(input('Digite o Numero para saber a sua tabuada até 10: '))
print(f'Essa é a Tabuada de {numero}')
for c in range(0, 11):
    resultado = numero * c
    print(f'{numero} x {c} = {resultado}')