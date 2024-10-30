from random import randint
v = 0
while True:
    jogador = int(input('A :'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('P ou I')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador} Total de {total}')
        print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
        if tipo == 'P':
            if total % 2 == 0:
                print('YOU WIN!')
                v+=1
            else:
                print('YOU LOSE!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('YOU WIN!')
            else:
                print('YOU LOSE!')
                break

print('SE FUDEU!')