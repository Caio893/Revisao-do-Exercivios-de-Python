pessoas = list()
cadastro = dict()
media = 0
while True:
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if cadastro['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M para Masculino ou F para Feminino.')
    cadastro['Idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    while True:
        parar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if parar in 'SN':
            break
        print('ERRO! Por favor, Responda Apenas S ou N.')
    if parar == 'N':
        break
for _, i in enumerate(pessoas):
    media += pessoas[_]['Idade']
media = media / len(pessoas)

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

print(f'B) A média de idade é de {media} anos.')

print(f'As mulheres cadastradas foram:')
for _ , i in enumerate(pessoas):
    if i['Sexo'] == 'F':
        print(i['Nome'].capitalize())

print(f'D) Lista das pessoas que estão acima da média: ')
for _, i in enumerate(pessoas):
    if i['Idade'] > media:
        for k, v in i.items():
            print(f'{k} = {v}')