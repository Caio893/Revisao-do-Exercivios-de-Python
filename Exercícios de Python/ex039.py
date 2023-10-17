import datetime

'''print('---Desagio 39---')
nascimento = int(input('Qual o ano de Nascimento do candidato:\n->'))
ano = datetime.datetime.today().year
sexo = str(input('Qual o seu sexo biologico M para Masculino e F para Feminino:\n->')).upper().strip()
servico = ano - nascimento
if sexo =="F":
    print(f'Você que é biologicamente mulher não precisa passar pelo alistamento obrigatório')
if servico == 18 and sexo == 'M':
    print('Você está com idade para o alistamento militar.')
elif servico > 18 and sexo == 'M':
    print(f'Você já passou da idade de alistamento você deveria ter ser alistado no ano de {ano + (18 - servico)}')
elif servico < 18 and sexo == 'M':
    print(f'Você ainda não está no ano de alistamento militar você deve voltar aqui no ano de {ano + (18 - servico)}')
print(f'Você esta com {servico} de idade.')'''

def verificar_alistamento(nascimento, sexo):
    ano_atual = datetime.datetime.today().year
    idade = ano_atual - nascimento
    
    if sexo == 'F':
        print(f'Você, bioloficamente do sexo feminino, não precisa passar pelo alistamento obrigatório')
    
    if idade == 18:
        print(f'Você está com idade para o alistamento militar.')
    elif idade > 18:
        ano_alistamento = ano_alistamento - (idade - 18)
        print(f'Você já passou da idade de alismento. Deveria ter se alistado em {ano_alistamento}.')
    else:
        ano_alistamento = ano_atual + (18 - idade)
        print(f'Você ainda não está na idade de alistamento militar. Volte aqui no ano de {ano_alistamento}')

def main():
    print('---Desafio 39 (Aprimorado)---')
    nascimento = int(input('Qual o ano de nascimento do candidato: '))
    sexo = str(input('Qual o seu sexo biológico (M para Masculino e F para Feminino): ')).strip().upper()
    
    mensagem = verificar_alistamento(nascimento, sexo)
    print(mensagem)
    
if __name__ == "__main__":
    main()