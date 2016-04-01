import pygame
from pygame.locals import *
from sys import exit

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
text_color = (10, 10, 10)

def main() :

    #Initialize Screen
    pygame.init()
    SCREEN_DIMENSIONS = (150,50)
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS) # create screen
    pygame.display.set_caption("Hello World Pygame")

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert() # make into single pixel format
    background.fill(WHITE) 

    # Create and display some text
    our_font = pygame.font.Font(None, 35)
    text = our_font.render("Hello World", 1, text_color)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx

    # Render text to background and background to screen
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True :

        for event in pygame.event.get() :
            if event.type == QUIT :
                exit(0)

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == "__main__" :
    main()