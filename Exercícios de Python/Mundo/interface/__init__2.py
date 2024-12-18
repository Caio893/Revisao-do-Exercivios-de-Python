def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erri na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')




def lerAquivo(nome):
   try:
       a = open(nome, 'rt')
   except:
       print('Erro ao ler o arquivo!')
   else:
       cabeçalho('PESSOAS CADASTRADAS')
       for linha in a:
           dado = linha.split(';')
           dado[1] = dado[1].replace('\n','')
           print(f'{dado[0]:<30}{dado[1]:>3} anos')
   finally:
       a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('HOUVE UM ERRO NO ARQUIVOR NA HORA DE ABRIR')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('houve outro erro')
        else:
            print(f'Novo resgitro de {nome} adicionado.')
            a.close()