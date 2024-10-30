soma = 0
contador = 0
t = int(input('Digite o termo: '))
r = int(input('Digite a Razão: '))
pa = 0
for c in range(0, 10):
    t += r
    print(f'{t-r}',end=' -> ')
print(f'ACABOU')



##Resposta certa é a formula décimo = t + (10 - 1) * r