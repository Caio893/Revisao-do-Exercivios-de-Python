from time import sleep
def contagem(a,b,d):
    for n in range(a,b,d):
        print(f'{n}', end=' ')
        sleep(0.3)
    print(f'{b}', end=' ')
    print('FIM !')


print('-='*30)
print('Contagem de 1 até 10 em 1 em 1')
for c in range(1, 11, 1):
    sleep(0.3)
    print(f'{c}', end=' ')
print()
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
for c2 in range(10, -2, -2):
    sleep(0.3)
    print(f'{c2}', end=' ')
print()
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = passo + 1
if fim < 0:
    passo = passo + (-passo*2)
if inicio > fim and passo > 1:
    passo = passo + (-passo*2)


contagem(a=inicio, b=fim, d=passo)
