from datetime import datetime
contador = 0
maior = 0
menor = 0
atual = datetime.today().year
for c in range(0, 7):
    contador += 1
    nascimento = int(input(f'Qual o ano de nascimento da {contador}ª: '))
    if atual - nascimento < 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {menor}ª com mais de 18 anos')
print(f'Ao todo tivemos {maior}ª com menos de 18 anos de idade')