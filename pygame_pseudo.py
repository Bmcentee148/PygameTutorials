[load modules]

[resource handling functions]

class Ball :

    [ball functions go here]
    [e.g. a function to move the ball]
    [e.g. a function to see if ball hit the sides]


def main() :

    [initiate game environment here]

    [create new ball object from Ball class]
    ball = Ball()

    # Main event loop
    while True :

        [check for user input]

        [call Balls update function] -> use before blitting onto screen
        ball.update()