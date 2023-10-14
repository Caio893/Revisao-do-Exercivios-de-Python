print('--Desafio 28---')
from random import randint
pc = randint(1, 10)
pessoa = int(input('Vamos jogar um jogo, eu estou pensando em um numero de 1 até 10 me diga qual é esse numero: '))
if pessoa == pc:
    print(f'Acertou misseravel você disse {pessoa} e eu pensei exatamente {pc} como você sabia ?')
else:
    print(f'Errou você disse {pessoa} e eu pensei em {pc} tente novamente.')
