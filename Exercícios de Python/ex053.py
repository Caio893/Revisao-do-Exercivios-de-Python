frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto ="".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
    print(junto, inverso)
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um palíndromo')
'''print('---Desafio 53---') #fiz do meu jeito sem for
nome = str(input('Diga um nome ou palavra para vermos se é PALÍNDROMO\n-> ')).upper().strip().replace(" ", "")
palidromo = nome[::-1]
if nome == palidromo:
    print(f'É um Palíndromo {palidromo}')
else:
    print(f'A palavra não é um Palíndromo {nome} e {palidromo} ')
print(palidromo)
print(nome)'''