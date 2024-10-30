primeiro = int(input('Digite o Termo: '))
razao = int(input('Digite a Razao: '))
termo = primeiro
cont = 0
desativado = False
mais_termos = 0
tottermos = 0
total = 0
cont2 = 10
while not desativado:
    for cont in range (0, cont2):
        print(f'{termo}', end=' ')#Nota Memória ordem das linhas influencia a laço antes o laço come com 5 pq a string com print estava depois do acumulador e isso causava um problema na hora de mostrar a ordem certa na saida. print depois do laço de acumulaodr dava 5 10 25 20 antes de começar o acumulador começa com 0.
        cont += 1
        termo += razao
        tottermos += 1
    total += termo
    mais_termos = int(input('\nMais quantos termos você deseja ver: '))
    cont2 = mais_termos
    if mais_termos == 0:
        desativado = True
print(tottermos)