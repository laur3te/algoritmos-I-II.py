import pygame  
file = '021.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
input()
pygame.event.wait()