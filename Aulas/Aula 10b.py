nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print(f'Bom dia {nome}!')

n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua segunda nota '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m == 10:
    print('PQP CARALHO TA COM MÉDIA 10 MLK')
if m >=6.0:
    print('Parabéns sua nota está acima da média!')
else:
    print('Você precisa estudar mais!')
print('PARABÉNS' if m >=6.0 else 'ESTUDA MAIS')