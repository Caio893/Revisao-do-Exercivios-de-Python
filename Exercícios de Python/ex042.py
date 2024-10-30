import math
a = float(input('Entre com o valor do lado a: '))
b = float(input('Entre com o valor do lado b: '))
c = float(input('Entre com o valor do lado c: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print(f'EQUILÁTERO')
    elif a == b != c or b == c != a or a == c != b:
        print(f'ISÓSCELEES')
    elif a != b != c:
        print(f'ESCALENO')
else:
    print(f'Não forma um triangulo')