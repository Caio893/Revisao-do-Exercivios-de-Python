lista_price = ('1.75', '2.00', '15.90', '25.00', '4.20', '9.99', '120.32', '22.30', '34.90')
lista_nome = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
nome = 0
print('-'*50)
print('LISTA DE PREÇOS'.center(50))
print('-'*50)
for c in lista_nome:
    print(f'{c:<1}','.'*20, f'R${lista_price[nome]}'.center(0))
    nome +=1
print('-'*50)