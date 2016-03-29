# Opens a blank pygame window. Good to use as a template for new programs.
# @author Brian McEntee

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

pygame.init()

# Set width and height of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Text Rotate")

# Loop until user clicks the closed button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

text_rotate_degrees = 0
# --------- Main Program Loop -------------
while not done :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True

    # ----- Game Logic Goes Here -----

    # ----- Screen Clearing Code Goes Here -----

    screen.fill(WHITE)

    # ----- Drawing Code Goes Here -----

    #Borders
    pygame.draw.line(screen, BLACK, [100,50], [200,50])
    pygame.draw.line(screen, BLACK, [100,50], [100,150])

    #Font 
    #font = pygame.font.SysFont('Calibri', 25, True, False)

    #Sideways Text
    #text = font.render("Sideways Text", True, BLACK)
    #text = pygame.transform.rotate(text, 90)
    #screen.blit(text,[0,0])
    # ----- Update Screen With What Was Drawn
    pygame.display.flip()

    # ----- Limit to 60 frames a second
    clock.tick(60)

# Close the window and quit
pygame.quit()
