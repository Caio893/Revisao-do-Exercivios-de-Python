name = str(input('Digit your name: '))
name2 = str(name).strip().split()
print(f'\nHello {name}'
      f'\nYour First name is {name2[0]}'
      f'\nAnd your last name is {name2[-1]}')
