print('Reforço para os burros')
#Inpts para as variaveis 
a = int(input('Digite um valor 1\n ->'))
b = int(input('Digite um valor 2\n ->'))
c = int(input('Digite um valor 3\n ->'))
d = int(input('Digite um valor 4\n ->'))
e = int(input('Digite um valor 5\n ->'))
f = int(input('Digite um valor 6\n ->'))

#Criando as variaveis maior e menor para o print
maior = a
menor = a

# Conferindo e atribuindo o maior a variavel.
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e
if f > maior:
    maior = f

# Conferiando e atribuindo o menor a variavel

if b < menor:
    menor = b
if c < menor:
    menor = c
if d < menor:
    menor = d
if e < menor: 
    menor = e
if f < menor:
    menor = f
    
print(f'O Maior número é o {maior}\nE o menor número é o {menor}')