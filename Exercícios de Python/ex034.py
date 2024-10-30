salario = float(input('Qual o seu salário: '))
if salario > 1250.00:
    aumento = (salario * 10/100)
    salario = aumento + salario
    print(f'Seu novo salario é de {salario} tendo um aumento de {aumento}')
else:
    aumento = (salario * 15/100)
    salario = salario + aumento
    print(f'Seu novo salario é de {salario} tendo um aumento de {aumento}')

