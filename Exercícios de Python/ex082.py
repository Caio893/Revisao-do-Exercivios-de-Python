# Inicializa as listas
valores = []
pares = []
impares = []

# Loop para entrada de dados
while True:
    n = int(input('Digite um número: '))
    valores.append(n)  # Adiciona o número à lista principal

    # Verifica se o número é par ou ímpar
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    # Pergunta se o usuário deseja continuar
    stop = input('Digite S para parar a contagem ou qualquer outra tecla para continuar: ').strip().lower()
    if stop == 's':
        break

# Exibe os resultados
print(f'Os valores digitados foram: {valores}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')

''''valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um numero: ')))
    stop = str(input('Digite S para parar a contagem: ')).strip().lower()
    if 's' in stop:
        break
for _, i in enumerate(valores):
    if i % 2 == 0:
        pares.append(i)
    if i % 2 != 0:
        impares.append(i)
print(f'Os valores digitados foram {valores}'
      f'\nOs numeros pares são {pares}'
      f'\nOs numeros ímpares são {impares}')'''