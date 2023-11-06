print(f'Desafio 61'.center(16,"%"))
primeiro = int(input('Digite o primeiro termo da P.A\n ->'))
razão = int(input('Digite a razão da sua P.A\n ->'))
c = 0
while c < 9:
    primeiro += razão
    c += 1
    print(primeiro, end=' > ')
c = int(input('Quantos termos você quer mostrar a mais\n ->'))
print('FIM')