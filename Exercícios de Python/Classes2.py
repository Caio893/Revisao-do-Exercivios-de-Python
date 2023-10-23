class ContaBancaria:
    
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar (self, valor):
        self.saldo += valor
        return f'Depositou {valor}'
    
    def sacar (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f'Sacou {valor}'
        else: 
            return 'Saldo Insuficiente'
        
    def consultar_saldo(self):
        return f'{self.saldo}'


conta = ContaBancaria("Caio Marcio", 5000)
print(f'{conta.titular} Saldo:{conta.consultar_saldo()}')

valor_deposito = float(input('Quanto você quer depositar'))

print(conta.depositar(valor_deposito))
print(f'Novo Saldo: {conta.consultar_saldo()}')

valor_saque = float(input('Quanto você quer sacar?'))
print(conta.sacar(valor_saque))
print(f'Novo saldo: {conta.consultar_saldo()}')        
    
''''class ContaBancaria: # Falha minha
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self):
        float(input('Qualto você quer depositar:\n->'))
        return 'Depositou {depositar}'
    def sacar(self):
        float(input('Quanto você quer sacar:\n->'))
        return 'Sacou {sacar}'
    def consultar_saldo(self):
        print(f'{self.saldo}')

conta = ContaBancaria("Caio Márcio", 50000)
print(f'{conta.titular} Saldo {conta.saldo} vai depositar {conta.sacar} {conta.consultar_saldo} {conta.depositar}')
'''