# Import a library of functions called 'pygame'
import pygame
import sys
import drawablenode
from drawablenode import *
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 25
COLS = 25
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

NODES = {}
for i in range(ROWS):
    for j in range(COLS):
        NODES[str([i, j])] = DrawableNode(i, j)

'''NODES = []
for i in range(ROWS):
    for j in range(COLS):
        node = search_space.get_node([i, j])
        NODES.append(DrawableNode(node))'''

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.Font(None, 14)
font2 = pygame.font.Font(None, 28)
selnode = NODES["[0, 0]"]
while not DONE:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    # CLOCK.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop

        if pygame.key.get_pressed()[pygame.K_w]: #When the w key is pressed, move up
            if selnode.posy >= 0:
                selnode = NODES[str([selnode.posx, selnode.posy - 1])]
                print "w"

        if pygame.key.get_pressed()[pygame.K_a]: #When the a key is pressed, move left
            if selnode.posx >= 0:
                selnode = NODES[str([selnode.posx - 1, selnode.posy])]
                print "a"

        if pygame.key.get_pressed()[pygame.K_s]: #When the s key is pressed, move down
            if selnode.posy >= 0:
                selnode = NODES[str([selnode.posx, selnode.posy + 1])]
                print "s"

        if pygame.key.get_pressed()[pygame.K_d]: #When the d key is pressed, move right
            if selnode.posx >= 0:
                selnode = NODES[str([selnode.posx + 1, selnode.posy])]
                print "d"

    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(WHITE)
    # Draw a circle
    for i in NODES:
        NODES[i].draw(SCREEN, font1)

    #Draws a circle, showing where you, the user, is on the grid
    pygame.draw.circle(SCREEN, WHITE, (selnode.screenpos[0] + 25, selnode.screenpos[1] + 25), 10)

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.
    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
