print('--Desafio 30--')
distancia = float(input('Qual a distancia da sua viagem:\n-->'))
if distancia <=200.0:
    print(f'A sua viagem de {distancia}Km sai a R${distancia*0.50}')
else:
    print(f'Sua viagem de {distancia} sai a R${distancia*0.45}')
print('Obrigado pela preferencia')
