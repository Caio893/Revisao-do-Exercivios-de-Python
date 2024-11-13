from time import sleep
def cadastro():
        while True:
            print('-' * 50)
            print('MENU PRINCIPAL'.center(50))
            print('-' * 50)
            print(f'1 - Ver pessoas cadatradas'
                  f'\n2 - Cadastrar nova Pessoa'
                  f'\n3 - Sair do Sistema')
            print('-' * 50)
            try:
                option = int(input('Escolha uma opção: '))
                if option == 3:
                    print('-' * 50)
                    print('Saindo do sistema... Até logo!'.center(50))
                    print('-' * 50)
                    return option
                else:
                    print('-' * 50)
                    print(F'OPÇÃO {option}'.center(50))
                    print('-' * 50)
                    sleep(2)
                    return option
            except(ValueError, TypeError):
                print(f'ERRO! não é uma opção válida.')
                sleep(2)
                continue
            except(KeyboardInterrupt):
                print(f'Programa Finaliza')
                sleep(2)
                break

cadastro()