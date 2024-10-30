valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    stop = str(input('Aperte S para parar a contagem: ')).lower().strip()
    if stop == 's':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} Valores'
      f'\nOs valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')