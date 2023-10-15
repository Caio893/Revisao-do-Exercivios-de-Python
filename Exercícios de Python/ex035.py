print('--Desafio 35--')
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if (b - c) < a < b + c and (a - c) <b < a + c and (a - b) < c < a + b:
    print('É possivel fazer um Triangulo')
else:
    print('Não é possivel formar um triangulo')
print(19//2)