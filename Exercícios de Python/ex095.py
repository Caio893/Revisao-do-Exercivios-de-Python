time = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou?: '))
    for c in range(jogador['Partidas']):
        gols.append(int(input(f'   Quantos na {c+1} Partida: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resp in 'N':
        break

print('-=' *30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' *40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    jogado = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if jogado == 999:
        break
    if jogado >= len(time):
        print(f'ERRO! tente de 0 até {len(time)}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[jogado]['Nome']}')
        for _, g in enumerate(time[jogado]['Gols']):
            print(f'No jogo {_} fez {g} gols.')
print('-'*40)
