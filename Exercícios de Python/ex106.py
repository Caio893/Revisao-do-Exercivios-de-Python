from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO !!!', 1)

'''def ajuda(nome):
    print('\033[0;34m~\033[m' * 30)
    print(f'\033[0;34mAcessando o manual do campo {nome}\033[m')
    print('\033[0;34m~\033[m' * 30)
    return f'\031[0;31m{help(nome)}\031[m'
def título(msg, cor):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

while True:
    print('\033[0;34mSISTEMA DE AJUDA pyHELP\033[m')
    ajudar = str(input('\033[0;34mFunção ou Biblioteca> \033[m'))
    if 'fim' in ajudar:
        break
    else:
        ajuda(ajudar)
'''