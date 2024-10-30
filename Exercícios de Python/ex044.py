valor1 = float(input('Informe o valor da compra: '))
print('Escolha qual opção de pagamento.'
      '\n[1]à vista dinheiro/cheque'
      '\n[2]à vista cartão'
      '\n[3]2x no cartão'
      '\n[4]3x ou mais no cartão')
option = int(input('Forma de Pagamento: '))
if option == 1:
    valor = valor1 - (valor1 * 10/100)
    print(f'Sua compra de {valor1} vai sair a {valor}')
elif option == 2:
    valor = valor1 - (valor1 * 5/100)
    print(f'Sua compra de {valor1} vai sair a {valor}')
elif option == 3:
    print(f'Sua compra fica a {valor1}')
elif option == 4:
    valor = valor1 + (valor1 * 20/100)
    print(f'Sua compra de {valor1} vai sair a {valor}')