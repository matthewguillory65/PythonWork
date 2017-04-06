from pygame import *
import math
from VectorMath import *
import random
from GameAI import *

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255,165,0)
RAINBOW = (random.randrange(100, 200), random.randrange(100, 200), random.randrange(100, 200))
RED = (255, 0, 0)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
deltatime = CLOCK.get_time()
Target = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
circles = []

for i in range(500):
    circles.append(AIpoint(Vector(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))))

DONE = False
while not DONE:
    CLOCK.tick(40)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop
        if event.type == pygame.MOUSEMOTION:
            Target.x, Target.y = pygame.mouse.get_pos()

    #Updates the circles that follow Target
    for i in circles:
        i.ApplyForce(i.Steering(Target), deltatime)
        i.UpdatePos()
        if i.position.x >= SCREEN_WIDTH:
            i.position.x = SCREEN_WIDTH
        if i.position.y >= SCREEN_HEIGHT:
            i.position.y = SCREEN_HEIGHT
        if i.position.x <= 0:
            i.position.x = 0
        if i.position.y <= 0:
            i.position.y = 0
        

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(BLACK)
    
    for i in circles:
        pygame.draw.circle(SCREEN, (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), (int(i.position.x), int(i.position.y)), 22)
    pygame.draw.circle(SCREEN, RED, (Target.x, Target.y), 15)

    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 6))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()