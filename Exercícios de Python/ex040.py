def notas_aluno(nota1, nota2):
    media = (nota1 + nota2) / 2
    
    if media < 5.0:
        print(f'Sua média foi {media} Reprovado você precisa estudar mais!')
    elif media >= 5.0 and media <= 6.9:
        print(f'Sua média foi {media} Recuperação continue estudando para tirar uma nota melhor!')
    elif media >= 7.0:
        print(f'Sua média foi {media} Aprovado mas estude para tirar 10!')
        
def main():
    print('---Desafio 40---')
    nota1 = float(input('Qual a primeira nota do aluno:\n->'))
    nota2 = float(input('Qual a segunda nota do aluno\n->'))
    
    mensagem = notas_aluno(nota1, nota2)
    print(mensagem)
    
if __name__ == "__main__":
    main()