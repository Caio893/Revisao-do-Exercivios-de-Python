def aumentar(preço=0, taxa=0, show=False):
    """
    Função para aumentar o valor de um float em x%.
    :param preço: valor do float a ser passado
    :param taxa: a porcentagem que vai ser informanda.
    :param show: mostra se quer formado chamando a função moeda
    :return: retorna o valor com o aumento da porcentagem informada
    """
    res = preço + (preço * taxa/100)
    if show:
        return moeda(res)
    return res


def diminuir(preço=0, taxa=0, show=False):
    """
    Função para diminuir o valor de um float em x%
    :param preço: valor do float a ser passado
    :param taxa: a porcentagem que vai ser informado
    :param show: mostra se que formatado chamando a função moeda
    :return: retorna o valor com a diminuição da porcentagem informada
    """
    res = preço - (preço * taxa/100)
    if show:
        return moeda(res)
    return res


def dobro(preço=0, show=False):
    """
    Função para dobrar o valor de um float
    :param preço: valor do float a ser passado
    :param show: mostra se que formatado chamando a função moeda
    :return: retorna o dobro do valor
    """
    res = preço * 2
    if show:
        return moeda(res)
    return res


def metade(preço=0, show=False):
    """
    Função para dividir pela metade o valor de um float
    :param preço: valor do float a ser passado
    :param show: mostra se que formatado chamando a função moeda
    :return: retorna metade do valor
    """
    res = preço / 2
    if show:
        return moeda(res)
    return res


def moeda(preço=0, moeda='R$'):
    """
    formata o retorno das funções com R$ e , em vez de .
    :param preço: valor do retorno das funções
    :param moeda: e o tipo de moeda se é US dolar ou R$ real
    :return: retorna ela formatada
    """
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, desconto=0):
    """
    faz tudo que já foi mencionado acima só que em 1 função chamando todas as outras anteriores.
    :param novo_preço: recebe o valor e que vai ser passado para outra função
    :param aumento: recebe o valor que vai ser passado para função de aumento em %
    :param desconto: recebe o valor que vai ser passado para função de dimiuir em %
    :return: retorna todas as funções acima formatadas.
    """
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{desconto}% de redução: \t{diminuir(preço, desconto, True)}')
    print('-' *30)