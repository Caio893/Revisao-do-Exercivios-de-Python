print('Desafio 23')
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidade {u}\n'
      f'Dezena {d}\n'
      f'Centena {c}\n'
      f'Milhar {m}\n')
