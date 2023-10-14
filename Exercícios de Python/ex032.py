print('--Desafio 33--')
import datetime
ano = int(input('Qual ano você gostaria de sabe que é bissexto?\n--> '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} É um ano bissexto')
else:
    print(ano)