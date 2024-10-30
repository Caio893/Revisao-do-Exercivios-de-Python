lado_a = float(input('Qual o lado a: '))
lado_b = float(input('Qual o lado b: '))
lado_c = float(input('Qual o lado c: '))
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c and lado_a > lado_b:
    print(f'Os lados formando um tirangulo')
else:
    print(f'Não é possivel forma um triangulo com esses lados')