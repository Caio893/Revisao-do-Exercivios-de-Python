print('Desafio 58'.center(16, '#'))

from random import randint

print('Olá sou seu computador configurado em código pobre e ruim, tente adivinhar qual número o radint colocou no minha variavel.')

pc = randint(0, 10)
player = int(input('Qual o número você acha que o PC está pensando ?\n-> '))
tentativas = 0

while player != pc:
    print(f'Tente novamente parece que o PC não pensou nesse número!')
    if player > pc:
        print(f'Menos... Tente novamente')
    else:
        print(f'Mais... Tente novamente')
    player = int(input('->'))
    tentativas += 1
print(f'Parabéns você acertou o PC estava pensando em {pc} e você escreveu {player}'
      f' Foram necessária {tentativas} tentativas')
