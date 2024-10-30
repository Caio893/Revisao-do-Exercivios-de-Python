numero =  list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor add...')
    else:
        print('Valor duplicado! Não adicionado.')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'N':
        break
numero.sort()
print(f'Você digitou of valores {numero}')
'''numeros = []
repetido = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    stop = str(input('Quer continuar ? aperte N para parar ou aperte enter: ')).strip().upper()
    if 'N' in stop:
        break
for _, c in enumerate(numeros):
    repetido = numeros.count(c)
    if repetido >= 2:
        numeros.remove(c)
numeros.sort()
print(f'Aqui a lista dos número digitados {numeros}')
'''