print('---Desafio 34---')
salario = float(input('Digite seu salário para sabermos o aumento que ele vai receber.\n ->'))
if salario > 1250.00:
    aumento = salario + (salario * 10/100)
    print(f'Seu salário de R${salario} teve um aumento de 10% e ficou em R${aumento}')
else:
    aumento = salario + (salario * 15/100)
    print(f'Seu salário de R${salario} teve um aumento de 15% e ficou um total de R${aumento}')