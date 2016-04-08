# Import statements 
try :
    import pygame
    import math
    import sys
except ImportError as err :
    print err
    sys.exit(1)

# Define some colors as implied constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Other Constants we localize to control in one place
BG_COLOR = BLACK
PADDLE_WIDTH = 30
PADDLE_HEIGHT = 10
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Paddle class definition 
class Paddle(pygame.sprite.Sprite) :

    def __init__(self, color, width, height) :
        # Call super-constructor
        pygame.sprite.Sprite.__init__(self)
        # Create and fill surface for object then draw rectangle on it
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get area of current game screen 
        curr_screen = pygame.display.get_surface()
        self.area = curr_screen.get_rect()
        # Get rectangle of the image, used for moving object
        # Update position changing rect.x and rect.y or use rect.move(x,y)
        self.rect = self.image.get_rect()
        # Reinitialize speed and position of paddle
        self.reinit()
        
    def update(self) :
        pass

    def reinit(self) :
        self.rect.midbottom = self.area.midbottom
# end class Paddle




# Main Event Loop
def main() :

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(BG_COLOR)
    screen.blit(background, [0, 0])
    pygame.display.flip()

    game_paddle = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_sprite = pygame.sprite.RenderPlain(game_paddle)

    while True :
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                print "User has ended play."
                sys.exit(0)

        screen.blit(background, game_paddle.rect, game_paddle.rect)
        game_paddle.update()
        paddle_sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__" :
    main()



