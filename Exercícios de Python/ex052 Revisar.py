nome = str(input('Digite a palavra: ')).strip().upper()
splitar = nome.split()
junto = ''.join(splitar)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
    print(junto[letra])
if inverso == junto:
    print('Pali')
else:
    print('Não é')