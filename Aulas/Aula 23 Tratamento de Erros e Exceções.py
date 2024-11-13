try:
    a = int(input('Númeor: '))
    b = int(input('Detonimador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'O erro foi o Tipo de dados.')
except ZeroDivisionError:
    print('Erro na divisão')
except KeyboardInterrupt:
    print('O usuário prefirui não informar os dados !')
except Exception as erro:
    print(f'O erro foi  {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Obrigado !!')