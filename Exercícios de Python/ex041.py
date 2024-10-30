from datetime import datetime
nascimento = int(input('Informe o ano de nascimento do candidato: '))
ano = datetime.today().year
idade = ano - nascimento
print(f'O Atleta tem {idade} anos')
if idade <= 9:
    print('MIRIN')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')