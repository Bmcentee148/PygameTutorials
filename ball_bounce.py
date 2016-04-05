import sys
import pygame

pygame.init()

BLACK = (0, 0, 0)

width = 640
height = 480
size = width, height

speed = [2, 2]

screen = pygame.display.set_mode(size)

ball = pygame.image.load('ball.bmp')
ball_rect = ball.get_rect()

clock = pygame.time.Clock()

while True :

    clock.tick(60)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit(0)


    ball_rect = ball_rect.move(speed)

    if ball_rect.left < 0 or ball_rect.right > width :
        speed[0] = -1 * speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height :
        speed[1] = -1 * speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.display.flip()

pygame.quit()

