print('===Desafio 04=== \nTestando tipos primitivos')
var = input('Digite alguma coisa.\n')
print(f'É um alfa numérico? {var.isalnum()} \nÉ um alfabeto? {var.isalpha()} '
      f'\nEstá em minusculo? {var.islower()} \nEstá em maiusculo? {var.isupper()} '
      f'\nEstá em capitalizada? {var.istitle()} \nO tipo desse primitivo é {type(var)}'
      f'\nTem espaço? {var.isspace()} \nÉ numérico? {var.isnumeric()}')