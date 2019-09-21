# hangman
# uses pygame-text-input: https://github.com/Nearoo/pygame-text-input

import pygame
import pygame_textinput
import logic 
import visuals

WIDTH = 800
HEIGHT = 600

def main():
    print("hang em good")



def hangman():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            logic.logic()
            visuals.visual(screen)
        
            

hangman()
