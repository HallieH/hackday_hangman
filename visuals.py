import pygame

def visual(screen):
    pygame.draw.circle(screen, pygame.Color(225,0,0), (400,400), 100)
    pygame.display.update()