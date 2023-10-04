print('Desafio 12')
produto = float(input('Qual o valor da mercadoria que você deseja o desconto de 5%: '))
desconto = (5/100)*produto
print(f'Com a promoção de 5% seu produto de R$ {produto} fica em R$ {produto - desconto:.2f} mais barato.')

##Forma correta que o professor ensinou é "preço - (preço * 5 / 100)"