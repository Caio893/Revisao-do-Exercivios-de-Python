import math

print('===Operadores Aritméticos===')
## + para Adição // Addition
## - para Subtração // Subtraction
## * para Multiplicação // Multiplication
## / para Divição // Division
## ** para Potência/Exponencial // Exponentiation
## // para Divisão Inteira // Floor Division
## % para resto da Divisão // Modulus
## == para ver se uma coisa é igual a outra no Python // Equal
## != Não é igual // No Equal
## > Maior que // Greater than
## <  Menor que // Less than
## >= Maior ou igual que // Greater than or equal to
## <=  Menor ou igual que // Less than or equal to
print(f'+ para Adição\n- para Subtração\n* para Multiplicação\n/ para Divição\n** para Potência/Exponencial\n'
      f'// para Divis o Inteira\n'
      f'% para resto da Divisã\n== para ver se uma coisa é igual a outra no Python ')
num1 =int(5+2)
num2 =int(5-2)
num3 =int(5*2)
num4 =float(5/2)
num5 =int(5**2)
num6 =int(5//2)
num7 =int(5%2)
print(num1, num2, num3, num4, num5, num6, num7)

##Ordem de Precedência para Programador
#1 () Parenteses sempre vai ser o primeiro a ser executado
#2 ** Potência/Exponencial é a segunda
#3 *,/,//,% Depois vem multiplicadoção divisão, divisão por inteniro e resto da divisão. Faz quem aparecer primeiro
#4 +,- Por ultimo faça a somana e subtração binária

#Exemplos:
# 5+3*2==11 Ordem de precedencia a multiplicação vem primeiro
# 3*5+4**2==31 Ordem de precedencia a Potência vem primeiro
# 3*(5+4)**2 Ordem de precedencia o parênteses vem primeiro
exemplo1 = int(5+3*2)
exemplo2 = int(3*5+4**2)
exemplo3 = int(3*(5+4)**2)
print(exemplo1, exemplo2, exemplo3)
print(math.sqrt(81))

##Você pode usar Operadores Aritméticos em str.
print('Gay'*5)

nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}')

nu1 = int(input('Digite um valor: '))
nu2 = int(input('Digite outro valor: '))
s = nu1 + nu2
m = nu1 * nu2
d = nu1 / nu2
di = nu1 // nu2
e = nu1 ** nu2
print(f'O resultado dos valores são{s}{m}{d}{di}{e}')
##para quebrar a linha \n
#para continuar a linha no print end='x'
