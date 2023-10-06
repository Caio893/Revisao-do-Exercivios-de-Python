import time

print('Desafio 21')
import pygame
pygame.init()
pygame.mixer.music.load('faz-o-l.wav')
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.quit()