number = int(input('Digit a number: '))
number_str = str(number)
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print(f'\nUnidade {u}'
      f'\nDezena {d}'
      f'\nCentena {c}'
      f'\nMilhar {m}')

##print(f'\nUnidades {number_str[3]}' f'\nDezenas {number_str[2]}' f'\nCentenas {number_str[1]}' f'\nMilhar {number_str[0]}')

