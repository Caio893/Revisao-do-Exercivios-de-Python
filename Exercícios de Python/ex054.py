print('---Desafio 54---')
import datetime
pessoas = int(input('São quantas pessoas ? '))
ano_atual = datetime.datetime.today().year
maior = 0
menor = 0
for c in range(pessoas):
    nascimento = int(input('Qual o ano de nascimento de cada umas delas: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
    
print(f'Tem {maior} pessoas maior de idade')
print(f'Tem {menor} pessoas menores de idade')

