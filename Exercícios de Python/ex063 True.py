cont = totcont = 0
stop = False
while not stop:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        stop = True
    else:
        cont += n1
        totcont += 1
print(f'Você digitou {totcont} e a soma entre eles foi {cont}')

