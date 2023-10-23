class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def cumprimentar(self):
        print(f'{self.nome} Cumprimenta você')
    
    def ano_de_nascimento(self):
        ano_atual = 2023
        return ano_atual - self.idade
    
pessoa1 = Pessoa("Aline", 35)
pessoa2 = Pessoa("Bob", 40)

pessoa1.cumprimentar()
print(f'{pessoa1.nome} Nasceu em {pessoa1.ano_de_nascimento()}')

pessoa2.cumprimentar()
print(f'{pessoa2.nome} Nasceu em {pessoa2.ano_de_nascimento()}')

