#O encapsulamento é o princípio de esconder os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso geralmente é alcançado por meio do uso de modificadores de acesso, como público, privado e protegido. Aqui está um exemplo de encapsulamento em Python:
    
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

# Criando uma conta bancária
minha_conta = ContaBancaria("João", 1000)

# Tentando acessar diretamente um atributo privado (Isso não é recomendado)
# print(minha_conta.__saldo)  # Isso geraria um erro

# Acessando atributos e métodos por meio da interface pública
minha_conta.depositar(500)
minha_conta.sacar(200)
print(f"Saldo da conta de {minha_conta.get_titular()}: R${minha_conta.get_saldo()}")

#O encapsulamento é o princípio de esconder os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso geralmente é alcançado por meio do uso de modificadores de acesso, como público, privado e protegido. Aqui está um exemplo de encapsulamento em Python: