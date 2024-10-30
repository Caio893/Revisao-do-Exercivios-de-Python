aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de  {aluno["nome"]:} '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')


'''aluno = dict()
alunos = list()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
alunos.append(aluno.copy())
print(f'O nome é igual a {aluno["nome"]}\nA média é igual a {aluno["media"]}')
if aluno['media'] <= 6:
    print('Situação é igual Reprovado')
else:
    print('Situação é igual Reprovado')'''