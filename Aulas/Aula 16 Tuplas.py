food = ('Hambuger', 'Juice', 'Pizza', 'Flan')
print(food)
print('TUPLAS SÃO IMUTAVEIS !!!!')
print(food[:4])
print(food[:-3])
print(len(food))
for count2 in food:
    print(f'Eu vou comer {count2}')
for cont in range(0,len(food)):
    print(f'Eu vou comer {food[cont]}, {cont}')
for pos, c in enumerate(food):
    print(f'I will eat {c}, na posição {pos}')
print(sorted(food))
print(food)

a = (2, 5, 4)
b = (5, 8 ,1 ,2)
print(a)
print(b)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
c2 = b + a
print(c2)
print(c2.index(5))
print(sorted(c2))
pessoa = ('Gustavo' , 39, 'M', 99.88)
print(pessoa)