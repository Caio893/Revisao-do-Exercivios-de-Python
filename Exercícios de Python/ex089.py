ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' *26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO....')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        print('<<< VOLTE SEMPRE >>>')

'''alunos = [[],[],[]]
alunos_nota = [[],[],[]]
n = 0
tot = 0
tot2 = 0
while True:
    total = 0
    media = 0
    alunos_nota[0].append(str(input('Nome: ')))
    for c in range(2):
        n = float(input(f'Nota {c}: '))
        alunos_nota[1].append(n)
        total += n
        media = total / 2
    alunos_nota[2].append(media)
    alunos[0].append(alunos_nota[0][:])
    alunos[1].append(alunos_nota[1][:])
    alunos[2].append(alunos_nota[2][:])
    alunos_nota[0].clear()
    alunos_nota[1].clear()
    alunos_nota[2].clear()
    tot += 1
    stop = str(input(f'Quer continuar ? [S/N] ')).lower().strip()
    if stop in 'Nn':
        break
print(f'No. Nome         Média')
print('-'*50)
for c in range(tot):
    print(f'{c}  ', end='')
    print(f'{alunos[0][c]}              {alunos[2][c]}\n')
print('-'*50)
print(alunos)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'Notas de {alunos[0][n]} as notas dele foram {alunos[1][n]}')
'''