from random import randint
sorte = randint(0, 10)
jogada = 0
tentativas = 0
while sorte != jogada:
    jogada = int(input('Digite o numero que o PC está pensando: '))
    if jogada < sorte:
        print(f'Tente um número maior que {jogada}')
        tentativas += 1
    if jogada > sorte:
        print(f'Tente um numero menor que {jogada}')
        tentativas += 1
print(f'Você acertou o número que o PC estava pensando era {sorte} '
      f'Você levou {tentativas} para acerta')