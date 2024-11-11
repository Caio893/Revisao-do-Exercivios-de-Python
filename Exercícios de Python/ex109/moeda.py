def aumentar(preço=0, taxa=0, show=False):
    res = preço + (preço * taxa/100)
    if show == True:
        return moeda(res)
    return res


def diminuir(preço=0, taxa=0, show=False):
    res = preço - (preço * taxa/100)
    if show == True:
        return moeda(res)
    return res


def dobro(preço=0, show=False):
    res = preço * 2
    if show == True:
        return moeda(res)
    return res


def metade(preço=0, show=False):
    res = preço / 2
    if show == True:
        return moeda(res)
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')


