brasileirao = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional' ,'Bahia', 'Cruzeiro',
               'Vasco', 'Atlético-MG', 'Grêmio', 'Criciúma', 'Bragantino', 'Juventude', 'Athletico-PR', 'Fluminense',
               'Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')
print(f'Lista de times do Brasileirão {brasileirao[:5]}')
print(f'Lista dos 5 últimos colocados no Brasileirão {brasileirao[-5:]}')
print(f'Lista do Brasileirão em ordem alfabética{sorted(brasileirao)}')
print(f'O time do Bragantino está em {brasileirao.index("Bragantino")+1}ª colocação')