jogador = dict()
gols = list()
quantidade = 0
while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Partidas'] = int(input(f'Quantas Partidas {jogador["Nome"]} jogou?: '))
    for c in range(jogador['Partidas']):
        gols.append(int(input(f'Quantos gols na {c+1} Partida: ')))
    for c, i in enumerate(gols):
        quantidade += i
    jogador['Partidas'] = gols[:]
    jogador['Total'] = quantidade
    break
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O Campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador jogou {len(jogador["Partidas"])} partidas')
for c in range(len(jogador["Partidas"])):
    print(f'=> Na partida {c+1}, fez {jogador["Partidas"][c]} gols.')
print(f'E foi um total de {quantidade} Gols')
# Usa sum() para somar o total da lista de gols ou de algum valor sem precisar per correr o array com for.