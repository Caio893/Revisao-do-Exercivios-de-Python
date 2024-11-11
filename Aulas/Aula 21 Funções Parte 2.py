def soma(a=0,b=0,c=0):
    s = a + b + c
    return s


r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)

print(f'Meus cálculos são {r1} {r2} {r3}')


'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vela {a}')



def contador(i,f,p):
    """Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funç~ao criada por Caio Márcio
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(0,100,10)
help(contador)

def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(1,2,3)
somar(10)
somar(b=20)
somar(c=30)
somar()



def teste(b):
    b += 4
    c = 2
    a = 8
    print(f'Na função teste, n vale {n}')
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
#programa principal
n = 2
a = 5
print(f'No programa principal, n vale {n}')

teste(a)

print(f'A fora vale {a}')'''