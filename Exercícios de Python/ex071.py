print('BANCO GUANABARA')
cedula50 = cedula10 = cedula1 = 0
while True:
    money = int(input('Valor: '))
    while money >= 50:
        cedula50 += 1
        money -= 50
    while money >= 10:
        cedula10 += 1
        money -= 10
    while money >= 1:
        cedula1 += 1
        money -= 1
    print(f'{cedula50} {cedula10} {cedula1}')
    if money == 0:
        break