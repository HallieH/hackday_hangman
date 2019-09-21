import pygame

def visual(screen):
    pygame.draw.line(screen, pygame.Color(153, 76, 0), (50, 100), (50, 450), 10)#main pole
    pygame.draw.line(screen,  pygame.Color(153, 76, 0), (0, 450),(200,450), 50)#base
    pygame.draw.line(screen, pygame.Color(153, 76, 0), (50, 104), (300, 104), 10)#outreach of pole
    pygame.draw.line(screen, pygame.Color(153, 76, 0), (297, 100), (297, 155), 10)#pole holding rope
    pygame.draw.line(screen, pygame.Color(227, 227, 227), (297, 155), (297, 175), 1)#rope to man
    pygame.draw.circle(screen, pygame.Color(225, 174, 97), (297,205), 30)#head
    pygame.draw.line(screen, pygame.Color(225, 174, 97), (297,230),(297,340), 1)#body
    pygame.draw.line(screen, pygame.Color(225, 174, 97), (297,340),(334,430), 1)#left leg
    pygame.draw.line(screen, pygame.Color(225, 174, 97), (297,340),(260,430), 1)#right leg
    pygame.draw.line(screen, pygame.Color(225, 174, 97), (297,255),(277,330), 1)#Left arm
    pygame.draw.line(screen, pygame.Color(225, 174, 97), (297,255),(317,330), 1)#right arm


    pygame.display.update()
    