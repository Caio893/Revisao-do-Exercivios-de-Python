from datetime import datetime
nascimento = int(input('Digite o ano de nascimento: '))
atual = datetime.today().year
idade = atual - nascimento
if idade == 18:
    print('Você está no de se Alistar')
elif idade < 18:
    print(f'Você ainda não está na idade de se alistar {(atual -idade) + 18}')
elif idade > 18:
    print(f'Você já passou da idade de alistamento o ano para você se alistar era em {(atual - idade) + 18}')
print(idade)