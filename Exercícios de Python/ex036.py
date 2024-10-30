casa = float(input('Digite o Valor da Casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Vai pagar em quantas parcelas: '))

parcelas = casa / (anos*12)

if parcelas > (salario * 30/100):
    print(f'Seu Empréstimo não foi aprovado.')
elif parcelas <= (salario * 30/100):
    print(f'Seu Empréstimo foi APROVADO !!!!')
else:
    print(f'ERRO TENTE NOVAMENTE.')

print(f'{parcelas}')
print(casa/anos)
print(salario * 30/100)

