num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

'''par = []
impar = []
valores = list()
for p in range(7):
    p = int(input('Digite um valor: '))
    if p % 2 == 0:
        par.append(p)
    if p % 2 != 0:
        impar.append(p)
valores.append(impar[:])
valores.append(par[:])
valores[0].sort()
valores[1].sort()
print(f'Os valores impares foram {valores[0]}')
print(f'Os valores pares foram {valores[1]}')
'''