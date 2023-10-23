import random
print('---Desafio 45---')

jogador = str(input('PEDRA\nPAPEL\nTESOURA\n->')).strip().upper()

pc = random.randint(1,3)
if pc == 1:
    pc2 = 'PEDRA'
elif pc == 2:
    pc2 = 'PAPEL'
elif pc == 3:
    pc2 = 'TESOURA'

if pc2 == 'PEDRA' and jogador == 'TESOURA':
    print(f'Quem venceu foi o PC pois jogou {pc2} e o Jogador {jogador}')
    
elif jogador =='PEDRA' and pc2 == 'TESOURA':
    print(f'Quem venceu foi o Jogador pois jogou {jogador} e o PC {pc2}')
    
elif pc2 == 'TESOURA' and jogador =='PAPEL':
    print(f'Quem venceu foi o PC pois jogou {pc2} e o Jogador {jogador}')
elif jogador =='TESOURA' and pc2 == 'PAPEL': 
    print(f'Quem venceu foi o Jogador pois jogou {jogador} e o PC {pc2}')
    
elif pc2 == 'PAPEL' and jogador =='PEDRA':
    print(f'Quem venceu foi o PC pois jogou {pc2} e o Jogador {jogador}')
    
elif jogador =='PAPEL' and pc2 == 'PEDRA':
    print(f'Quem venceu foi o Jogador pois jogou {jogador} e o PC {pc2}')
    
elif pc2 == jogador:
    print(f'EMPATE')

##print(f'PC {pc2} x {jogador} Jogador ')
print(pc2)
print(pc)

'''import random #chatGPT

print('---Desafio 45---')

# Crie uma lista com as opções para o PC
opcoes_pc = ['PEDRA', 'PAPEL', 'TESOURA']

# Solicite a escolha do jogador e verifique se é uma opção válida
jogador = input('Escolha: PEDRA, PAPEL, ou TESOURA -> ').strip().upper()
if jogador not in opcoes_pc:
    print('Escolha inválida. Por favor, escolha PEDRA, PAPEL ou TESOURA.')
else:
    # Use random.choice para selecionar a escolha do PC
    pc2 = random.choice(opcoes_pc)
    
    print(f'PC escolheu: {pc2}')
    print(f'Jogador escolheu: {jogador}')

    if pc2 == jogador:
        print('EMPATE')
    elif (
        (pc2 == 'PEDRA' and jogador == 'TESOURA') or
        (pc2 == 'TESOURA' and jogador == 'PAPEL') or
        (pc2 == 'PAPEL' and jogador == 'PEDRA')
    ):
        print(f'PC venceu! {pc2} vence {jogador}')
    else:
        print(f'Jogador venceu! {jogador} vence {pc2}')
'''