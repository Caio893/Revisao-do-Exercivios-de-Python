from math import trunc ##Corta da virgula para frente o numero
print('Desafio 16')
num = float(input('Digite um numero real ou flutuante: '))
inteiro = trunc(num)
print(inteiro)

##math.trunc(x) Return x with the fractional part removed, leaving the integer part. This rounds toward 0: trunc() is
# equivalent to floor() for positive x, and equivalent to ceil() for negative x. If x is not a float, delegates to
# x.__trunc__, which should return an Integral value.