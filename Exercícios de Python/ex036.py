print('---Desafio 36---')
casa = float(input('Digite o valor da casa que você deseja avalair:\n->'))
salario = float(input('Qual o seu salário mensal:\n->'))
anos = float(input('Em quantos anos você pretende pagar as parcelas da sua casa nova :\n->'))
parcelas = casa / (anos * 12)
salarioterço = salario * 30/100
if parcelas > salarioterço:
    print(f'Não foi aprovado pois excede 30% do seu salário mensal. ')
else:
    print(f'Aprovado')
print(f'Para pagar uma casa de R${casa} em {anos} anos.\n'
      f'a prestação será de R${parcelas:.2f}')