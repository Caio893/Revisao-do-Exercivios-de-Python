frase = str('Curso em Video Python')
print(f'{frase[9:13]}')
##Aqui ele só vai mostrar a letra que fica no espaço 9 da stringe lembrando que em python começa
# do 0 e ele contra como um valor então se tiver 20 letra contando junto com o 0 vai ter 21.
# Ultilizando o :13 ele vai do 9 ao 12 no print pois ele ignora o ultimo caracter
print(f'{frase[9:21]}') # Começa no 9 e vai até o final msm se não tive o 21. Não é amelhor forma
print(f'{frase[9:21:2]}') # Começa no 9 para no 21 e vai pulando de 2 em 2
print(f'{frase[:5]}') # :5 Quando você omite o inicio ele vai começar do inicio até o 5
print(f'{frase[15:]}') # Quando você omite o final ele vai até o final
print(f'{frase[9::3]}') # Quando você coloca o inicio omite o segundo e coloca um 3 ele vai pular de 3 em 3 Tipo Video vai ser (VePh)
print(f'{len(frase)}') # len em é um metodo para dizer quando caracteres tem em um string muito importante gravar.
print(f'{frase.count("o")}') # frase.count serve para contar quando 'x' letra numeros seja oque for em use "" aspas duplas para não confundir o python
print(f'{frase.count("o",0,13)}') # Aqui ele vai contar quantos "o" tem começando do 0 até o 13 vai dar 1 pq lembrando ele ignora o ultimo valor.
print(f'{frase.find("deo")}') # Aqui ele vai buscar "deo" e vai dizer o local aonde COMEÇA a posição no exemplo ele deo começa no caracter 11.
print(f'{frase.find("Android")}') # Nesse exemplo ele vai usar a função find para buscar a palavra "Android" e dizer onde começa, como não existe essa palvra na nossa variavel string ele retornar -1
print(f'{"Curso" in frase}') # Esse operado me retonar True ou False, no que esta escrito em "x" exemplo "Curso" se ele achar o que ta escrito vai retornar o valor Verdadei o Falso
print(frase.replace("Python","Android")) # Transfomação via de regra uma lista de string ela é imutavel, mas é possivel usar metodo para alterar a string como no exemplo x.replace("x","y") aqui ele muda a variavel de forma secundaria
print(frase.upper()) # Aqui ele vai colocar TUDO em maiusculo é muito importante usar esse metedo
print(frase.lower()) # Aqui faz a mesma coisa que upper mas coloca tudo que tiver maiusculo em minusculo msm imporancia
print(frase.capitalize()) # Aqui ele só coloca a primeira letra da string para maiusculo e o resto fica minusculo.
print(frase.title()) # aqui diferente de capitaliza ele vai coloca a letra maiuscula em cada palavra. Quebrando em espaços.
print(frase.strip()) # É o santo metodo que remove todos os espaços inuteis no inicio e no final da string
print(frase.rstrip()) #Faz a mesma coisa só que só que remove os espaços só da direita
print(frase.lstrip()) #Mesma coisa só que da esquerda
print(frase.split()) # Ele vai pegar cada palavra que esta com espaço entre ela e organizar com virgula e aspas e com isso recomeça a contagem em cada palavra gerando uma lista com cada palavra com contagem de 0 até o final.
print("-".join(frase)) # Ele vai separar e colocar "x" em cada letra da string e espaço que tiver disponivel.
print("-".join(frase.split())) #Aqui combinante Split que separou cada palavra da string em uma nova lista ele simplesmente colocou um - entre cada lista nova.
print(frase.upper().strip()[::2].split()) #Aqui mostra tudo só que pulando de 2 em 2
print(len(frase))
frase = frase.replace("Curso", "Viado") #Agora sim ele salvou as alterações em replace na nova variavel e vai mostrar oque foi alterado quando eu der o print
frase = frase.upper().strip()
print(frase)
print('VIADO' in frase)
print(frase.find("VIADO"))
dividido = frase.split()
print(dividido[2][3])
frase = "Python é uma linguagem poderosa"
palavras = frase.split(" ", maxsplit=2)  # Divide a string em até 2 partes
print(palavras)  # Saída: ['Python', 'é', 'uma linguagem poderosa']
# Neste caso, a string foi dividida em até 2 partes, e o restante da string foi mantido intacto como parte do último elemento da lista.
print('Essas são algumas das maneiras comuns de usar o método split() em Python para dividir strings ou sequências em partes com base em um separador.')