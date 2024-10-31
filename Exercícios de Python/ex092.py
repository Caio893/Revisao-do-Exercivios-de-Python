cadastro = {}
from datetime import datetime
while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = int((input('Ano de Nascimento: ')))
    cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        break
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = int(input('Salário: R$'))
    calculo = (cadastro['Contratação'] + 35) - cadastro['Idade']
    cadastro['Aposentadoria'] = calculo
    cadastro['Idade'] = datetime.now().year - cadastro['Idade']
    break

for k, v in cadastro.items():
    print(f'- {k} tem valor {v}')