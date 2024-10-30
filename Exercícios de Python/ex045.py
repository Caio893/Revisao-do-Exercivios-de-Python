from random import choice

jogador = int(input('Suas Opções\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\nQUAL A SUA JOGADA: '))
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if jogador == 1:
    jogador = str('PEDRA')
elif jogador == 2:
    jogador = str('PAPEL')
elif jogador == 3:
    jogador = str('TESOURA')

if pc == 'PEDRA' and jogador == 'TESOURA':
    print(f'PC ESCOLHEU {pc}PC WIN')
elif pc == 'PAPEL' and jogador == 'TESOURA':
    print(f'PC ESCOLHEU {pc} PERDEU')
elif pc == 'TESOURA' and jogador == 'TESOURA':
    print(f'PC ESCOLHEU {pc} EMPATE')
if pc == 'PEDRA' and jogador == 'PEDRA':
    print(f'PC ESCOLHEU {pc}EMPATE')
elif pc == 'PAPEL' and jogador == 'PEDRA':
    print(f'PC ESCOLHEU {pc} PC WIN')
elif pc == 'TESOURA' and jogador == 'PEDRA':
    print(f'PC ESCOLHEU {pc} PERDEU')
if pc == 'PEDRA' and jogador == 'PAPEL':
    print(f'PC ESCOLHEU {pc} PERDEU')
elif pc == 'PAPEL' and jogador == 'PAPEL':
    print(f'PC ESCOLHEU {pc} EMPATE')
elif pc == 'TESOURA' and jogador == 'PAPEL':
    print(f'PC ESCOLHEU {pc} PC WIN')