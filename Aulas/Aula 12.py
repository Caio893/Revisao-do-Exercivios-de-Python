nome = str(input('Qual é o seu nome ?\n->'))
if nome == 'Gustavo':
    print('Que nome bonito"')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popula no Brasil!')
elif nome in 'Anna Clárdia Jéssica Juliana':
    print('Seu nome é bem popular.')
else:
    print('Seu nome é bem normal.')
    
print(f'Tenha um bom dia {nome}')