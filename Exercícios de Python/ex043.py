def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    if imc <= 18.5:
        print(f'Você tem {imc:.1f} de IMC e você esá abaixo do peso.')
    elif imc <= 25:
        print(f'Você tem {imc:.1f} de IMC e você está no peso ideal')
    elif imc <=30:
        print(f'Você tem {imc:.1f} de IMC e você está com sobre peso')
    elif imc <=40:
        print(f'Você tem {imc:.1f} de IMC e você está com Obesidade')
    else:
        print(f'Você tem {imc:.1f} de IMC e você esta com Obesidade Mórbida')

def main():
    print(f'---Desafio 42---')
    try:
        peso = float(input('Qual o seu peso\n-> '))
        altura = float(input('Qual a sua altura\n->'))
        
    except ValueError:
        print(f'Por Favor insira valores numéricos válidos para altura e peso. Use . pontos e não vírgulas')
    
    resultado = calcular_imc(peso, altura)
    print (resultado)
    
if __name__ == "__main__":
    main()
    
'''# Constantes para as faixas de IMC #chat GPT
IMC_ABAIXO_PESO = 18.5
IMC_PESO_IDEAL = 25
IMC_SOBREPESO = 30
IMC_OBESIDADE = 40

def calcular_imc(peso, altura):
    """
    Calcula o IMC e retorna a categoria correspondente.
    """
    imc = peso / altura ** 2
    if imc <= IMC_ABAIXO_PESO:
        return f'Você tem {imc:.1f} de IMC e você está abaixo do peso.'
    elif imc <= IMC_PESO_IDEAL:
        return f'Você tem {imc:.1f} de IMC e você está no peso ideal.'
    elif imc <= IMC_SOBREPESO:
        return f'Você tem {imc:.1f} de IMC e você está com sobrepeso.'
    elif imc <= IMC_OBESIDADE:
        return f'Você tem {imc:.1f} de IMC e você está com obesidade.'
    else:
        return f'Você tem {imc:.1f} de IMC e você está com obesidade mórbida.'

def main():
    print('---Desafio 42---')
    try:
        peso = float(input('Qual o seu peso (em kg):\n-> '))
        altura = float(input('Qual a sua altura (em metros):\n-> '))
    except ValueError:
        print('Por favor, insira valores numéricos válidos para altura e peso. Use . para separar decimais em vez de vírgula.')
        return

    resultado = calcular_imc(peso, altura)
    print(resultado)

if __name__ == "__main__":
    main()
'''