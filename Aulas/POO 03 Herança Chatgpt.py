# Herança: A herança é um dos princípios fundamentais da Programação Orientada a Objetos (POO) que permite criar novas classes com base em classes existentes, herdados seus atributos e métodos. Isso ajuda a reutilizar código e estabelecer relacionamentos hierárquicos entre classes. Vamos ver um exemplo de herança em Python

# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

# Classes derivadas (subclasses)
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} diz Woof!"

class Gato(Animal):
    def falar(self):
        return f"{self.nome} diz Meow!"

# Criando objetos
meu_cachorro = Cachorro("Rex")
minha_gata = Gato("Mia")

# Chamando o método falar nas subclasses
print(meu_cachorro.falar())  # Saída: "Rex diz Woof!"
print(minha_gata.falar())    # Saída: "Mia diz Meow!"

# Neste exemplo, temos uma classe base chamada Animal com um construtor que aceita um nome e um método falar. Em seguida, criamos duas subclasses, Cachorro e Gato, que herdam da classe Animal e fornecem sua própria implementação do método falar. Isso demonstra como a herança permite que as subclasses compartilhem características da classe base, mas também tenham comportamento específico.

#Herança é uma maneira poderosa de criar hierarquias de classes e promover a reutilização de código, pois as subclasses podem herdar atributos e métodos da superclasse e adicionar ou substituir comportamentos específicos.