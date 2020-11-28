import pygame

pygame.mixer.init()
tempo = pygame.time.Clock()

pygame.mixer.music.load("C:\\Users\\ander\\Music\\Kasatka.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    print('Tocando...')
    tempo.tick(1)