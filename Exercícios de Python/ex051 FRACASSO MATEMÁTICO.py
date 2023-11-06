primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}')
    print(décimo)
print('ACABOU')
print(décimo)










''''print('---Desafio 51---')
cumulo = 0
cumulo2 = 0
termo = int(input('Digite o primeiro termo\n-> '))
progressao = int(input('Digite a Razão\n-> '))
for progressao in range(10):
    cumulo = termo + progressao

cumulo += termo + progressao
cumulo2 += 0 == cumulo

print(cumulo2)'''