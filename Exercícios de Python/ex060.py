termo = int(input('Digite o Termo: '))
razao = int(input('Digite a Razão: '))
limite = 9
print(f'{termo}', end='')
while limite != 0:
    limite -= 1
    contador = termo + razao
    print(f' -> {contador}',end=' ')
    termo = contador
print('FIM!')