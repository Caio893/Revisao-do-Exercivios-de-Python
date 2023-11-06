primeiro_termo = int(input('Qual o primeiro termo da P.A\n -> '))
razão = int(input('QUal a razão da P.A\n -> '))
termo = primeiro_termo
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        cont +=1
        termo += razão
        print(f'{termo}', end=' > ')
    print('PAUSA')
    mais = int(input('Quer ver mais\n-> '))





'''primeiro = int(input('Qual o primeiro termo da P.A\n ->')) #Primeiro valor a entrar para o calculo
razao = int(input('Qual a razão da sua P.A\n ->')) # razão e segundo valor
termo = primeiro # forma de simplificar ?
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo}',end=' > ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input(Quantos termos você que a mais))
print('FIM')'''