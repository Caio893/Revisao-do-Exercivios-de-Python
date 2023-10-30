print('Desafio 57'.center(16, "-"))
'''sexo = ''
while sexo != "M" and sexo != "F":
    sexo = input('Qual o sexo da pessoa. Digite M para Masculino ou F para Feminino.\n[M/F]:').upper().strip()[0] #o [0]Só esta pegando a primeira letra
    if "M" or "F":
        if sexo == 'M':
            print(f'O sexo mencionado foi Masculino')
        elif sexo == 'F':
            print(f'O sexo mencionado foi Feminino')
        else:
            print(f'Errado. {sexo} não é válido porfavor coloque M para Masculino ou F para Feminino')
print('FIM')'''
sexo = str(input('Qual é seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).split().upper()[0]
print(f'Seu {sexo} registrado com sucesso.')