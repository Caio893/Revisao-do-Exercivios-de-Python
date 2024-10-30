nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print(f'REPROVADO a média foi {media:.2f}')
elif media < 6.9:
    print(f'RECUPERAÇÃO a média foi {media:.2f}')
else:
    print(f'APROVADO a média foi {media:.2f}')
