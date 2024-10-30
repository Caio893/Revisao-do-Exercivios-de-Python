from random import randint
pc = randint(0,10)
rodadas = 0
fim = 0
while True:
    jogada1 = int(input('Digite seu numero para a jogada: '))
    jogada2 = str(input('Aperte P para PAR ou I para Ímpar [P/I]: ')).upper().strip()[0]
    resultado = pc + jogada1
    while True:
        if jogada2 == 'P' and resultado % 2 == 0:
            print(f'Você venceu o pc jogou {pc} e você {jogada1} o total foi {resultado} PAR!!!')
            rodadas += 1
            break
        elif jogada2 == 'P' and resultado % 2 == 1:
            print(f'Você perdeu o pc jogou {pc} e você {jogada1} o total foi {resultado} ÍMPAR !!!!')
            fim += 1
            break
        elif jogada2 == 'I' and resultado % 2 == 1:
            print(f'Você venceu o pc jogou {pc} e você {jogada1} o total foi de {resultado} ÍMPAR !!!!')
            rodadas += 1
            break
        elif jogada2 == 'I' and resultado % 2 == 0:
            print(f'Você perdeu o pc jogou {pc} e você {jogada1} o total foi de {resultado} PAR !!!!!')
            fim += 1
            break
    if fim == 1:
        break
    pc = randint (0, 10)
    print(resultado)
print(f'Você venceu {rodadas} vezes !')
print('FIM DE JOGO !!!')


#tipo = ' ' while tipo not in 'PI' isso me permite repetir a pergunta até o animal acertar