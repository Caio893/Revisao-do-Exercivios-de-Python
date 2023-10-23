class Produto:

    def __init__(self, nome, preço=10.0, quantidade=150.0):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
    def comprar(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            return f'Comprou {quantidade}'
        else:
            print(f'Não temos tudo isso em estoque.')
    def reabastercer(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
        else:
            print(f'Você tem {quantidade} desse produto você precisa reabastecer.')
    def calcular_valor_total(self):
       return self.quantidade * self.preço
    
# Criando uma instância da classe Produto
arroz = Produto("Arroz")
print(f'O Arroz custa {arroz.preço} e a quantidade em estoque é de {arroz.quantidade}')

comprar_arroz = int(input('Quantos sacos de arroz você quer comprar: '))
print(arroz.comprar(comprar_arroz))
print(f'Quantidade em estoque: {arroz.quantidade}')

estoque_arroz = int(input('Quantos sacos de arroz você quer reabastecer: '))
arroz.reabastercer(estoque_arroz)
print(f'Quantidade em estoque: {arroz.quantidade}')
print(f'Valor total do estoque: {arroz.calcular_valor_total()}')