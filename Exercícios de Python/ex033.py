n1 = int(input('Digite um número para saber qual é maior: '))
n2 = int(input('Digite um numero para saber qual é maior: '))
n3 = int(input('Digite um numero para saber qual é maior: '))
maior = n1>n2
menor = n1<n2
if n1 > n2 and n1 > n3:
    maior = n1
    print(f'{maior}')
if n2 > n1 and n2 > n3:
    maior = n2
    print(f'{maior}')
if n3 > n2 and n3 > n1:
    maior = n3
    print(f'{maior}')

if n1 < n2 and n1 < n3:
    menor = n1
    print(f'{n1} é o menor')
if n2 < n1 and n2 <n3:
    menor = n2
    print(f'{n2} é o menor')
if n3 < n1 and n3 <n2:
    print(f'{n3} é o menor')
    menor = n3