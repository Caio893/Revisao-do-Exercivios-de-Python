print('---Desafio 49---')
numero = int(input('Digite o número que você quer sabe a sua tabua.n\-> '))
for tabuada in range(0, 11, 1):
    resultado = numero * tabuada
    print(f'{numero} x {tabuada} = {resultado}')

print('FIM')