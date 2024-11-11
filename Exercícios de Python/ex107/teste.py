import moeda

p = float(input('Digite o preços: R$ '))
print(f'A metade R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
print(f'Diminuir 15%, temos R${moeda.diminuir(p,15)}')