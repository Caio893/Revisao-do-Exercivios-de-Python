contador = resultado = 0
while True:
    tabuada = int(input('Digite o numero para saber sua tabuada: '))
    if tabuada < 0:
        break
    while contador <= 10:
        resultado = tabuada * contador
        print(f"{tabuada} x {contador} = {resultado}")
        contador += 1
    contador = 0



