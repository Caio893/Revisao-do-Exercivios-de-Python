from random import randint
answer = int(input('Tente adivinhar qual número o computador está pensando.'
                   '\nDigite um número:'))
random = randint(1, 5)
if random != answer:
    print('Você errou tente novamente.')
else:
    print(f'Parabéns você acertou o computador pensou no número {random} e você {answer}')
print('Aperte Ctrl+F5 para jogar novamente.')
print(random)
