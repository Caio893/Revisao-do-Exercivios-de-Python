print('--Desafio 33--')
num1 = float(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 1->'))
num2 = float(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 2->'))
num3 = float(input('Digite um número para saber qual é o maior e menor entre eles:\n Número 3->'))
maior = [num1,num2,num3]
if num1 > num2 and num3 or num2 > num1 and num3 or num3 > num1 and num2:
    print(f'{maior} É o maior numero')