pessoas = {'nomes': 'Gustavo', 'sexo': 'M', 'idade':22}
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v  in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
print(pessoas.items())
pessoas['nomes'] = 'Leandro'
print(pessoas.items())
pessoas['peso'] = 98.5
print(pessoas.items())
brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(estado)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
estado3 = dict()
brasil2 = list()
for c in range(3):
    estado3['uf'] = str(input('Unidade Federativa: '))
    estado3['Sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(estado3.copy())
print(brasil2)
for e in brasil2:
        for k, v in e.items():
            print(f'O campo {k} tem valor {v}')
        for v2 in e.values():
            print(v2, end=' ')
        print()