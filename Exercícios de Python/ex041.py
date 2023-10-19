from datetime import datetime
def idade_atleta(nascimento, ano):
    idade = ano - nascimento
    
    if idade == 9:
        print(f'O Atleta tem {idade} anos de idade e ele vai jogar na categoria MIRIM')
    elif idade >= 10 and idade <= 14:
        print(f'O Atleta tem {idade} anos de idade e ele vai jogar na categoria INFANTIL')
    elif idade >=15 and idade <= 19:
        print(f'O Atleta tem {idade} anos de idade e ele vai jogar na categoria JÚNIOR')
    elif idade >= 20 and idade <= 25:
        print(f'O Atleta tem {idade} anos de idade e ele vai jogar na categoria SÊNIOR')
    elif idade > 25:
        print(f'O Atleta tem {idade} anos de idade e ele vai jogar na categoria MASTER')
    elif idade < 9:
        print(f'Ele não tem a idade minima para participar das partidas.')
    else:
        print(f'Você digitou o ano de nascimento de forma errado porfavor digite o ano de nascimento do atleta de forma correta.')
        
def main():
    print('---Desafio 41---')
    nascimento = int(input('Qual o ano de nascimento do atleta. Exemplo(1990)\n->'))
    ano = datetime.today().year
    
    mensagem = idade_atleta(nascimento, ano)
    print(mensagem)


if __name__ == "__main__":
    main()
    
    
    
    # O Código abaixo é o chatgpt
    '''from datetime import datetime

def categoria_atleta(ano_nascimento):
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento

    if idade < 9:
        return 'MIRIM'
    elif idade <= 14:
        return 'INFANTIL'
    elif idade <= 19:
        return 'JÚNIOR'
    elif idade <= 25:
        return 'SÊNIOR'
    else:
        return 'MASTER'

def main():
    print('---Desafio 41---')
    ano_nascimento = int(input('Qual o ano de nascimento do atleta (exemplo: 1990):\n->'))

    if ano_nascimento > ano_atual:
        print('Você digitou um ano de nascimento inválido.')
    else:
        categoria = categoria_atleta(ano_nascimento)
        print(f'O atleta está na categoria {categoria}.')

if __name__ == "__main__":
    main()
'''