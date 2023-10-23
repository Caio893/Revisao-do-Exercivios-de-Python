# O encapsulamento é o princípio de esconder os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso geralmente é alcançado por meio do uso de modificadores de acesso, como público, privado e protegido. Aqui está um exemplo de encapsulamento em Python:

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 5

    def status(self):
        print(f"Carro {self.marca} {self.modelo} do ano {self.ano} está a {self.velocidade} km/h.")

meu_carro = Carro("Ford", "Eco Sport", 2008)
meu_carro.acelerar()
meu_carro.status()

#Neste exemplo, a classe Carro é uma abstração de um carro real. Ela encapsula os detalhes relevantes, como marca, modelo, ano e velocidade, e fornece métodos para acelerar, frear e exibir o status. Isso torna mais fácil trabalhar com objetos do tipo carro em seu código.