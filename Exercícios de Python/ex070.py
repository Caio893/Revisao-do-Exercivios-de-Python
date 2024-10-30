compra = caro = barato = 0
barato_nome = ''
unidade = 0
print('LOJA SUPER BARATÃO')
while True:
    encerrar = ' '
    produto = str(input('Nome do Produto: ')).strip().upper()
    price = float(input('Preço: R$'))
    compra +=price
    unidade += 1
    if unidade == 1 or price < barato: #dica do professor
        barato = price
        barato_nome = produto
    if price > 1000:
        caro += 1
    while encerrar not in 'SN':
        encerrar = str(input('Deseja encerrar ? [S/N]: ')).strip().upper()[0]
    if encerrar == 'S':
        break
print(f'O total da compra foi R${compra}\n'
      f'Temos {caro} custando mais de R$1000.00 reais\n'
      f'O Produto mais barato foi {barato_nome} que custa {barato}')