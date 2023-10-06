print('Desafio 24')
cidade = str(input('Você nasceu na cidade de Santo? ')).strip().upper()
santo = cidade.split()
print(f'{"SANTO" in santo[0:1]}')
