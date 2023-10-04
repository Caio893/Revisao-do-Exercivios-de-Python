print('Desafio 13b')
produto = float(input('Qual o valor do seu produto R$:'))
parcelado = produto + (produto * 15/100)
vista = produto - (produto * 15/100)
print(f'Com parcelamento fica em R$:{parcelado} em até 4x de {parcelado/4}\n'
      f'Com pagamento a vista ele sai á R$:{vista}')