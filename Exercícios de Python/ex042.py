print('---Desafio 42---')
a = float(input('Digite o lado a\n->'))
b = float(input('Digite o lado b\n->'))
c = float(input('Digite o lado c\n->'))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a +b:
    print(f'É possivel forma um triangulo.')
    if a == b == c:
        print(f'Todos os lados são iguais então é um EQUILÁTERO')
    elif a != b !=c != a:
        print(f'Todos os lados são difereten então é um ESCALENO')
    else: 
        print(f'Um dos lados é diferente então é um ISÓSCELES')
else:
    print(f'Não é possivel forma um triangulo')

'''def is_triangle(a, b, c): # ChatGPT
    return (a + b > c) and (a + c > b) and (b + c > a)

def classify_triangle(a, b, c):
    if a == b == c:
        return "EQUILÁTERO"
    elif a == b or b == c or a == c:
        return "ISÓSCELES"
    else:
        return "ESCALENO"

def main():
    print('---Desafio 42---')
    a = float(input('Digite o lado a: '))
    b = float(input('Digite o lado b: '))
    c = float(input('Digite o lado c: '))

    if is_triangle(a, b, c):
        triangle_type = classify_triangle(a, b, c)
        print(f'É possível formar um triângulo do tipo {triangle_type}.')
    else:
        print('Não é possível formar um triângulo.')

if __name__ == "__main__":
    main()
'''