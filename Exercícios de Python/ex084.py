temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men == temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior eso foi de {mai}kg. peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}Kg.Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()


'''dados = list()
pessoas = list()
leves = list()
pesadas = list()
maior = []
menor = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    stop = str(input('Quer continuar? [S/N] ')).strip().lower()
    if 's' in stop:
        break
for p in pessoas:
    if p[1] <= 70:
        leves.append(p[0])
        menor.append(p[1])
    if p[1] >= 100:
        pesadas.append(p[0])
        maior.append(p[1])
maior.sort(reverse=True)
menor.sort()
print(f'Ao todo você cadastrou {len(pessoas)}.\n'
      f'O maior peso foi de {maior[0]}Kg. Peso de {pesadas[0]}\n'
      f'O menor peso foi de {menor[0]}Kg. Peso de {leves[0]}')'''

