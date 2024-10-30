for c in range(10,0,-1):
    print(c)
for c in range(100,10,-10):
    print(c)

numero = int(input('Digite um numero: '))
for c in range(1, numero+1):
    print(c)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
s = 0
for c in range(0,4):
    n = int(input('Digite um numero: '))
    s += n
print(f'O somatorio de todos os numeoros é {s}')