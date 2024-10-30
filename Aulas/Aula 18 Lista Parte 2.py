teste = list()
totmaior = totmenor = 0
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera2 = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(galera2[2][1])
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')
galera3 = list()
dados = list()
for c in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()
print(galera3)

for p2 in galera3:
    if p2[1] >= 21:
        print(f'{p2[0]} É maior de idade.')
        totmaior += 1
    else:
        print(f'{p2[0]} É maior de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')



'''dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
pessoas = list()
pessoas.append(dados[:])
print(pessoas)
pessoas = [['Pedro', 25],['Maria', 19],['João',32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''