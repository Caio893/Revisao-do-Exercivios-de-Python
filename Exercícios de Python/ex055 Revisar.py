totidade = 0
contador = 0
velho_homem = 0
nome_velho = ''
for c in range(0,5):
    sexo = str(input('Aperte F para Feminino e M para Masculino: ')).strip().upper()
    nome = str(input('Digite o Nome: ')).strip().upper()
    idade = int(input('Digite a Idade: '))
    totidade += idade
    if  c == 0 and sexo in 'M':
        velho_homem = idade
        nome_velho = nome
    if sexo in 'M' and idade > velho_homem:
        velho_homem = idade
        nome_velho = nome
    if idade < 20 and sexo == 'F':
        contador += 1

print(f'O homem mais velho é {nome_velho} e tem {velho_homem}')
print(f'Tem {contador} mulheres com menos de 20 anos')
print(f'A média de idade é de {totidade / 5}')