from gettext import dpgettext


def msg(txt):
    print('-='*30)
    print(f'{txt}')
    print('-='*30)

msg('Olá fdp!!!!')
msg('Não quero saber')

def soma(a, b):
    s = a + b
    print(s)
    print(f'A é igual a {a} e B é igual a {b}')

soma(b=4,a=6)
soma(1,6)
soma(9,5)

def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!!')
    tam = len(num)
    print(f'Recebi o valor de {num} e são {tam} numeros')

contador(2,5,6)
contador(2,5,6,3,4,2)
contador(1,6,7,3,2,6,3)


def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *=2
        pos += 1

valores = [6,7,8,5,5,6]
dobra(valores)
print(valores)

def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(4,7,8,9,5,6,9,58)
soma2(7,8,9,5,4,2,6,9,8,7)
