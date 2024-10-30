continuar = ''
media = totcont = totn1 = n1 = maior = 0
menor = 99999
while continuar != 'N':
    n1 = int(input('Digite um número: '))
    totn1 += n1
    totcont += 1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if maior < n1:
        maior = n1
    elif menor > n1:
        menor = n1
media = totn1 / totcont
print(f'Você digitou {totcont} números e a média foi de {media:.2f}'
      f' O maior valor foi {maior} e o menor valor foi {menor}')
#Nota mental não defina os dois valores de menor e maior antes da variável de controle num laço pois sempre vai ser alterado para o novo valor do laço então precisa ser dentro da varia de controle para mudar só quando bater com os requisitos do if.
'''if totcont == 1:
maior = menor = n1
else:
if n1 > maior:
    maior = n1
if n1 < menor:
    menor = n1'''
