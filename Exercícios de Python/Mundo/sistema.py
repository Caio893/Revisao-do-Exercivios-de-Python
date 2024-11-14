from time import sleep
from final import *
from interface import *

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
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(aqr, nome, idade)

    elif resposta == 3:
        print('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma Opção Válida\033[m')
    sleep(2)

