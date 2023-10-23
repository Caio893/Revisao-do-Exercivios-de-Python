#Neste exemplo, temos uma classe base Animal com um método fazer_som. As subclasses Cachorro e Gato sobrescrevem esse método para fornecer implementações específicas. A função fazer_barulho demonstra o polimorfismo, pois pode aceitar objetos de qualquer classe que seja uma subclasse de Animal e chamar o método fazer_som sobre eles de maneira uniforme.

#O polimorfismo torna o código mais flexível e extensível, pois permite que diferentes classes se comportem de maneira semelhante, facilitando a adição de novas classes que se encaixam na hierarquia existente.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz o som 'Woof!'"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz o som 'Meow!'"

# Função que demonstra polimorfismo
def fazer_barulho(animal):
    print(animal.fazer_som())

# Criando objetos das classes
rex = Cachorro("Rex")
mia = Gato("Mia")

# Chamando a função com objetos de classes diferentes
fazer_barulho(rex)  # Saída: "Rex faz o som 'Woof!'"
fazer_barulho(mia)  # Saída: "Mia faz o som 'Meow!'"

#Neste exemplo, temos uma classe base Animal com um método fazer_som. As subclasses Cachorro e Gato sobrescrevem esse método para fornecer implementações específicas. A função fazer_barulho demonstra o polimorfismo, pois pode aceitar objetos de qualquer classe que seja uma subclasse de Animal e chamar o método fazer_som sobre eles de maneira uniforme.

#O polimorfismo torna o código mais flexível e extensível, pois permite que diferentes classes se comportem de maneira semelhante, facilitando a adição de novas classes que se encaixam na hierarquia existente.