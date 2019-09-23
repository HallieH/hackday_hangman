# hangman
# uses pygame-text-input: https://github.com/Nearoo/pygame-text-input

import pygame
import pygame_textinput
import visuals
import random

WIDTH = 800
HEIGHT = 600

def main():
    print("hang em good")

idioms = ["A penny for your thoughts",
"Actions speak louder than words",
"Add insult to injury",
"Costs an arm and a leg",
"Back to the drawing board",
"Barking up the wrong tree",
"Beat around the bush",
"Best thing since sliced bread",
"Bite off more than you can chew",
"Devil's Advocate",
"Hit the nail on the head",
"Let sleeping dogs lie",
"Kill two birds with one stone",
"Let the cat out of the bag",
"Whole nine yards",
"Take with a grain of salt",
"Piece of cake",
"Cry over spilt milk",
"A Dime A Dozen",
"Close but no Cigar",
"Curiosity Killed The Cat",
"Head Over Heels"]

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
        
y = random.randint(0,21)
currentIdiom = idioms[y].lower()
mistakeslist = []
LinesForGuessing = []
for w in currentIdiom:
        if w == " ":
            LinesForGuessing.append(" ") 
        elif w == "'":
            LinesForGuessing.append("'") 
        else:
            LinesForGuessing.append("-") 

while len(mistakeslist) < 7:
    
    
    printthis = ""
    for element in LinesForGuessing:
        printthis = printthis+element
    print("Mistakes: ",len(mistakeslist))
    x = (input(("Guess one letter: ")))
    while len(x)!=1:
        x = input(("ONE letter dummy. Try again: "))
    count = 0
    hit = False
    for w in currentIdiom:
        if x == currentIdiom[count]:
            hit = True
            LinesForGuessing[count] = currentIdiom[count]
        count = count + 1
    if hit == False:
        mistakeslist.append(x) 
    printthis = ""
    for element in LinesForGuessing:
        printthis = printthis+element
    print(printthis)

    if "-" not in LinesForGuessing:
        print("YOU WIN")
        sys.exit()

print("YOU LOSE")
print(currentIdiom)
#hangman()
