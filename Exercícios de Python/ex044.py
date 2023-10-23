print('---Desafio 42---')
preço = float(input('Qual o valor do produto que você gostaria de comprar\n->'))
        
forma_de_pagamento = int(input('Escolha sua forma de pagamento.\n1 para pagamento à vista\n2 Para pagamento à vista no cartão\n3 para pagamento parcelado até 2x\n4 para pagamento parcelado no cartão em 3x ou mais.\n'))

vista = preço - (preço * 10/100)
vista_cartao = preço - (preço * 5/100)
parcelado = preço / 2
parcelado2 = preço + (preço * 20/100)
    
def pagamento(forma_de_pagamento):
   
    if forma_de_pagamento == 1:
        vista
        print(f'Pagando à vista o seu produto sai à R${vista:.2f}')
    elif forma_de_pagamento == 2:
        vista_cartao
        print(f'Pagando á vista no cartão o seu produto sai a R${vista_cartao:.2f}')
    elif forma_de_pagamento == 3:
        parcelado
        print(f'Pagando pacelado até 2x o seu produto sai a R${parcelado:.2f}')
    elif forma_de_pagamento == 4:
        parcelado2
        parcelamento = int(input('Quantas vezes?\n'))
        print(f'Pagando parcelado em {parcelamento} ou mais o seu produto sai a {parcelamento} de R${parcelado2 / parcelamento:.2f}')
    else:
        print('Erro tento uma das formas de pagamento.')
      
  
mensagem = pagamento(forma_de_pagamento)
print(mensagem)


'''def pagamento(preco, forma_de_pagamento): #chatGPT
    if forma_de_pagamento == 1:
        return preco - (preco * 0.10)
    elif forma_de_pagamento == 2:
        return preco - (preco * 0.05)
    elif forma_de_pagamento == 3:
        return preco / 2
    elif forma_de_pagamento == 4:
        parcelamento = int(input('Quantas vezes? '))
        return preco + (preco * 0.20), parcelamento

def main():
    print('---Desafio 42---')
    preco = float(input('Qual o valor do produto que você gostaria de comprar\n->'))
    
    forma_de_pagamento = int(input('Escolha sua forma de pagamento.\n1 para pagamento à vista\n2 Para pagamento à vista no cartão\n3 para pagamento parcelado até 2x\n4 para pagamento parcelado no cartão em 3x ou mais.\n'))

    if 1 <= forma_de_pagamento <= 4:
        resultado = pagamento(preco, forma_de_pagamento)
        if forma_de_pagamento == 4:
            valor, parcelamento = resultado
            print(f'Pagando parcelado em {parcelamento} vezes, o seu produto sai a {parcelamento} parcelas de R${valor / parcelamento:.2f}')
        else:
            print(f'Pagando à vista o seu produto sai a R${resultado:.2f}')
    else:
        print('Escolha uma das formas de pagamento válidas.')

if __name__ == "__main__":
    main()
'''