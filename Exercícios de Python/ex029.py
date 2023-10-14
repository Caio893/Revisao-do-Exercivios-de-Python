print('--Desafio 29--')
velocidade = float(input('Qual a velocidade do veículo: '.strip()))
multa = (velocidade-80)*7
acima = velocidade-80
if velocidade >=81.0:
    print(f'{velocidade}KM/h Você ultrapassou o limete de velocidade em {acima}KM/h vai ter que pagar R${multa} de multa')
else:
    print(f'{velocidade} Parabéns você está dentro do limete de velocidade.')

