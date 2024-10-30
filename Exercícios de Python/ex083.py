valores = list()
valores.append(str(input('Digite a equação para saber se ela está certa\nEquanção: ')))
valores[0].count('(')
for _, i in enumerate(valores):
    if valores[0].count('(') == valores[0].count(')'):
        print(f'Está certo')
    else:
        print(f'Está errado')