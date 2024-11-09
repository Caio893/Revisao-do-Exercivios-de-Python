def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
#Programa Principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))



'''from datetime import date
def voto():
    a = 'VOTO NEGADO'
    b = 'VOTO OBRIGATORIO'
    c = 'VOTO OPICIONAL'
    if nascimento <= 15:
        return a
    else:
        if nascimento <= 17:
            return c
        if nascimento >= 18:
            return b
        if nascimento <= 65:
            return c
n = int(input('Em que ano você nasceu? '))
nascimento = date.today().year - n
print(f'Com {nascimento} anos: {voto()}')
'''