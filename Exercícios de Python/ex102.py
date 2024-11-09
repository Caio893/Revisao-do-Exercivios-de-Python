def fatorial(n=1, show=False):
    """
    Calcula o Fatorial de um númeor.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{f} x {c} = ', end=' ')
    return f

print(fatorial(show=True))