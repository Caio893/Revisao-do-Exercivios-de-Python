menor_mulher = 0
totmaior = 0
tothomem = 0
while True:
    print('Cadastre uma pessoa')
    sexo = parada = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
    if 'M' in sexo:
        tothomem += 1
    if idade > 18:
        totmaior += 1
    if 'F' in sexo and idade < 20:
        menor_mulher += 1
    while parada not in 'SN':
        parada = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if parada == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmaior}\n'
      f'Ao todo temos {tothomem} homens cadastrados\n'
      f'E temos {menor_mulher} mulheres com menos de 20 anos.\n')