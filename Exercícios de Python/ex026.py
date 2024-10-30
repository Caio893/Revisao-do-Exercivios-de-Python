analise_string = str(input('Type something: ')).strip().upper()
print(f'\nThe letter A show {analise_string.count("A")}'
      f'\nThe first letter A aper. {analise_string.find("A")+1}'
      f'\nAnd the last letter A aper. {analise_string.rfind("A")+1}')

