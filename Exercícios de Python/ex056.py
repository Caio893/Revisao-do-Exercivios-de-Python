sexo = ''
totm = 0
totf = 0
while sexo != 'S': #Poderia ser While sexo not in 'MmFf' para repetir o laço
    sexo = str(input('Qual o sexo F para Feminino ou M para Masculino\n[F/M]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            totm += 1
        if sexo == 'F':
            totf += 1
    else:
        print('Errado tente M para Masculinou ou F para Feminino.')
print(f'O Total de Homens é de {totm} e de Mulheres é de {totf}')