peso = float(input('Digite o seu peso: '))
altura = float(input('Digite o seu peso: '))
imc = peso / altura**2
if imc < 18.5:
    print(f'Abaixo do peso seu imc é de {imc:.2f}')
elif imc < 25:
    print(f'Peso ideal seu imc é de {imc:.2f}')
elif imc < 30:
    print(f'Sobrepeso seu imc é de {imc:.2f}')
elif imc < 40:
    print(f'OBESO PORRA seu IMC é de {imc:.2f}')
else:
    print(f'OBESIDADE MÓRBIDA CARALHO PARA DE COMER !!! SEU IMC É DE {imc:.2f}')
