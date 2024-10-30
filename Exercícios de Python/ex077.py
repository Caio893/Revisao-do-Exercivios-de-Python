palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')



'''for c in palavras:
    print(f'Na palavra {c} temos ',end='')
    c = c.replace('P', ' ')
    c = c.replace('D', ' ')
    c = c.replace('N', ' ')
    c = c.replace('R', ' ')
    c = c.replace('M', ' ')
    c = c.replace('G', ' ')
    c = c.replace('L', ' ')
    c = c.replace('H', ' ')
    c = c.replace('C', ' ')
    c = c.replace('T', ' ')
    c = c.replace('Y', ' ')
    c = c.replace('S', ' ')
    c = c.replace('F', ' ')
    c = c.replace('B', '')
    c = c.replace(' ', '')
    print(f'{c.lower().strip()}')
'''