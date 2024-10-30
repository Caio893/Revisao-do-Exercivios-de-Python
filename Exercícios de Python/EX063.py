n1 = int(input('Digite um número: '))
fibo = 0
cont2 = 1
resultado = 0
cont = 0
while cont != n1:
    print(f'{resultado}->',end=' ')
    cont += 1
    resultado = fibo + cont2 #Aqui é o Resultado da soma inicial fibo como 0 e count como 2
    cont2 = fibo #Aqui o count2 armazena o fibo antes dele ter o valor alterado pelo resultado
    fibo = resultado #Aqui o fibo é alterado pelo resultado
print('FIM')
