#O que são classes?

#Em programação orientada a objetos (POO), as classes são estruturas que permitem modelar objetos do mundo real em um programa. Elas são uma forma de definir um "molde" ou "plano" para criar objetos que compartilham características comuns. Uma classe é composta por atributos (variáveis) e métodos (funções) que descrevem o comportamento dos objetos que serão criados a partir dela.

#Aqui está um exemplo simples de uma classe em Python:

class Carro:
    # Atributo da classe
    cor = "desconhecida"

    # Método da classe
    def ligar(self):
        print("O carro está ligado.")

# Criando um objeto (instância) da classe Carro
meu_carro = Carro()

# Acessando um atributo da classe
print("A cor do carro é:", meu_carro.cor)

# Chamando um método da classe
meu_carro.ligar()

#Neste exemplo, Carro é uma classe que tem um atributo cor e um método ligar. Quando você cria um objeto meu_carro a partir da classe Carro, ele herda as características da classe, como o atributo cor e o método ligar. Você pode acessar o atributo e chamar o método no objeto.

#Explicação do exemplo:

#Definimos a classe Carro usando a palavra-chave class.
#Dentro da classe, definimos o atributo cor e o método ligar.
#Criamos uma instância da classe Carro chamada meu_carro.
#Acessamos o atributo cor do objeto meu_carro usando a notação de ponto.
#Chamamos o método ligar no objeto meu_carro.
#Classes são fundamentais na programação orientada a objetos, pois permitem organizar e reutilizar código de forma eficiente, modelando objetos do mundo real em um programa. Elas ajudam a encapsular dados e funcionalidades relacionados em unidades autônomas e facilitam a manutenção do código à medida que os projetos crescem.