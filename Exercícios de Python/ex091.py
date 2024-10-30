from operator import itemgetter
from random import randint
from time import sleep
jogadores = dict()
for c in range(1,5):
    jogadores[f'jogador{c}'] = randint(1,6)
rank = list()
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('Ranking dos jogadores: ')
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)