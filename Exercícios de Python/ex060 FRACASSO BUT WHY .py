print('Desafio 60'.center(16, '+'))
from math import factorial
numero = int(input('Digite um número para sabermos seu fatorial\n->'))
c = numero
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)