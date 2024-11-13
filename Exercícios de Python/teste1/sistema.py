from teste2 import *
from arquivo import *
from time import sleep

arq = 'tabela.txt'
if not arqExiste(arq):
    criarArquivo(arq)
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma Opção Válida\033[m')
    sleep(2)

