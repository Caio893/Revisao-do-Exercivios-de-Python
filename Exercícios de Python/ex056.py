print('---Desafio 57---')
media_idade = 0
mulheres = 0
idade_homem = 0
nome_velho = ''

for c in range(1, 5):  # Iniciar o loop a partir de 1 para contar as pessoas de 1 a 4
    print(f'---{c}ª PESSOA---')
    nome = str(input('NOME\n->')).strip()
    idade = int(input('IDADE\n-> '))
    sexo = str(input('SEXO [M/F]\n->')).strip()

    media_idade += idade

    if sexo in 'Mm':
        if idade > idade_homem:
            idade_homem = idade
            nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulheres += 1

media = media_idade / 4
print(f'A média de idade é de {media:.0f} anos')
if nome_velho:  # Verifica se o nome do homem mais velho foi definido
    print(f'O Homem mais velho é o {nome_velho} e ele tem {idade_homem} anos')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, são {mulheres} mulheres com menos de 20 anos')
