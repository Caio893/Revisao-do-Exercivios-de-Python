print('Desafio 18')
import math
an = float(input('Digite o ângulo que você deseja? '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an}º tem o SENO de {seno:.2f}\n'
      f'O ângulo de {an}º tem o COSSENO de {cosseno:.2f}\n'
      f'O ângulo de {an}º tem a TANGETE de {tangente:.2f}\n')
