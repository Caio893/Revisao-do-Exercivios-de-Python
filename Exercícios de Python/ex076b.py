lista_mercado = ('Lápis', 1.75,'Borracha', 2.00,'Caderno', 15.90, 'Estojo', 25.00,'Transferidor', 4.20,
                 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print('LISTA DE PREÇOS'.center(50))
print('-'*50)
for c in range(0,len(lista_mercado), 2):
    print(f'{lista_mercado[c]:.<30}',end='R$')
    print(f'{lista_mercado[c + 1]:>7.2f}')
print('-'*50)