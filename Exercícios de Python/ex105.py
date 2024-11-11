def notas(*n, sit=False):
    """
    Função para criar um dicionário com as notas dos alunos.
    Nota Maior Menor e a Média com uma opção de True or False
    para mostrar a situação conforme a média do aluno.
    :param nota: encapsulamento de int para as notas
    :param show: opção para mostrar ou não situação da nota.
    :return: retorna o dicionario criado pela função.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)




'''def notas(*nota, show=False):
    """
    Função para criar um dicionário com as notas dos alunos.
    Nota Maior Menor e a Média com uma opção de True or False
    para mostrar a situação conforme a média do aluno.
    :param nota: encapsulamento de int para as notas
    :param show: opção para mostrar ou não situação da nota.
    :return: retorna o dicionario criado pela função.
    """
    alunos = dict()
    maior = menor = 0
    media = 0
    total = 0
    for k, v in enumerate(nota):
        media += v
        total += k
        alunos['Total'] = total
        if k == 0:
            maior = menor = v
            alunos['Maior'] = maior
            alunos['Menor'] = menor
        else:
            if v > maior:
                maior = v
                alunos['Maior'] = maior
            if v < menor:
                menor = v
                alunos['Menor'] = menor
    alunos['Média'] = media / len(nota)
    if show == True:
        if alunos['Média'] > 7:
            alunos['Situação'] = 'ÓTIMO'
        if alunos['Média'] > 5 < 6:
            alunos['Situação'] = 'BOM'
        if alunos['Média'] <= 4:
            alunos['Situação'] = 'RUIM'
        return alunos
    else:
        return alunos


resp = notas(10, 8, 4.5, show=True)
help(notas)'''