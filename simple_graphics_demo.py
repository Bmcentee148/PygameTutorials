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
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until user clicks the closed button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --------- Main Program Loop -------------
while not done :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True

    # ----- Game Logic Goes Here -----

    # ----- Screen Clearing Code Goes Here -----

    screen.fill(WHITE)

    # ----- Drawing Code Goes Here -----
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw an array of parallel lines using an offset in y direction 
    for y_offset in range(0, 100, 10) :
        pygame.draw.line(screen, BLUE, [0, 0 + y_offset], [100, 100 + y_offset], 5)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20,20,250,100], 2)

    # Draw an ellipse using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [20,20,250,100], 2)

    # Draw an ellipse via 4 arcs. Use radians to determine which part.
    pygame.draw.arc(screen, BLACK, [20,220,250,200], 0, PI / 2, 2)
    pygame.draw.arc(screen, RED, [20,220,250,200], PI / 2, PI , 2)
    pygame.draw.arc(screen, BLUE, [20,220,250,200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20,220,250,200], 3 * PI / 2, 2 * PI, 2)

    # Draw a triangle using the polygon function
    pygame.draw.polygon(screen, BLACK, [[350,250],[600,250],[475,150]], 3)

    pygame.draw.polygon(screen, BLACK, [[100,100],[0,200],[200,200]], 3)

    # Select font to use, size, bold, italics
    font = pygame.font.SysFont('Courier',25,True,False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250,250])

    # Update Screen With What Was Drawn
    # This MUST happen after all of the drawing commands
    pygame.display.flip()

    # Limit to 60 frames a second, otherwise we will all of cpu we can
    clock.tick(60)

# Close the window and quit
pygame.quit()
