# Import a library of functions called 'pygame'
import pygame
import sys
import drawablenode
from drawablenode import *
import random
import math

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 34
COLS = 18
WIDTH = 50
HEIGHT = 50
SCREEN_WIDTH = ROWS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = COLS * (PAD[0] + HEIGHT) + PAD[1]
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

NODES = {}
for i in range(ROWS):
    for j in range(COLS):
        NODES[str([i, j])] = DrawableNode(i, j)

for n in NODES:
    # Right
    if str([NODES[n].posx + 1, NODES[n].posy]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx + 1, NODES[n].posy])])
    # Up-Right
    if str([NODES[n].posx + 1, NODES[n].posy + 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx + 1, NODES[n].posy + 1])])
    # Up
    if str([NODES[n].posx, NODES[n].posy + 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx, NODES[n].posy + 1])])
    # Up-Left
    if str([NODES[n].posx - 1, NODES[n].posy + 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx - 1, NODES[n].posy + 1])])
    # Left
    if str([NODES[n].posx - 1, NODES[n].posy]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx - 1, NODES[n].posy])])
    # Down-Left
    if str([NODES[n].posx - 1, NODES[n].posy - 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx - 1, NODES[n].posy - 1])])
    # Down
    if str([NODES[n].posx, NODES[n].posy - 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx, NODES[n].posy - 1])])
    # Down-Right
    if str([NODES[n].posx + 1, NODES[n].posy - 1]) in NODES:
        NODES[n].adjacents.append(NODES[str([NODES[n].posx + 1, NODES[n].posy - 1])])

Start = NODES[str([0, 0])]
End = NODES[str([10, 10])]

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.Font(None, 14)
font2 = pygame.font.Font(None, 28)
selnode = NODES["[0, 0]"]

openList = []
closedList = []

currentnode = Start

openList.append(currentnode)

currentnode.g = 1
currentnode.h = abs(currentnode.posx - End.posx) + abs(currentnode.posy - End.posy)
currentnode.f = currentnode.g + currentnode.h



while not DONE:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    CLOCK.tick(15)

    if openList and currentnode != End:
        currentnode = openList[0]

        openList.remove(currentnode)
        closedList.append(currentnode)

        for neighbors in currentnode.adjacents:
            if neighbors not in closedList and neighbors.walkable:
                if neighbors not in openList:
                    openList.append(neighbors)
                neighbors.g = 1 + currentnode.g
                neighbors.h = abs(neighbors.posx - End.posx) + abs(neighbors.posy - End.posy)
                neighbors.f = neighbors.g + neighbors.h
                if neighbors.parent:
                    if neighbors.parent.g > currentnode.g:
                        neighbors.parent = currentnode
                else:
                    neighbors.parent = currentnode

        openList.sort(key = lambda n: n.f)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop

        if pygame.key.get_pressed()[pygame.K_w]: #When the w key is pressed, move up
            if selnode.posy - 1 >= 0:
                selnode = NODES[str([selnode.posx, selnode.posy - 1])]

        if pygame.key.get_pressed()[pygame.K_a]: #When the a key is pressed, move left
            if selnode.posx - 1 >= 0:
                selnode = NODES[str([selnode.posx - 1, selnode.posy])]

        if pygame.key.get_pressed()[pygame.K_s]: #When the s key is pressed, move down
            if selnode.posy + 1 < COLS:
                selnode = NODES[str([selnode.posx, selnode.posy + 1])]

        if pygame.key.get_pressed()[pygame.K_d]: #When the d key is pressed, move right
            if selnode.posx + 1 < ROWS:
                selnode = NODES[str([selnode.posx + 1, selnode.posy])]

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            selnode.walkable = not selnode.walkable

        if pygame.key.get_pressed()[pygame.K_n]:
            End = selnode
            openList = []
            closedList = []
            openList.append(Start)
            currentnode = Start
            for n in NODES:
                NODES[n].g = 0
                NODES[n].h = 0
                NODES[n].f = 0
                NODES[n].parent = None

        if pygame.key.get_pressed()[pygame.K_b]:
            Start = selnode
            openList = []
            closedList = []
            openList.append(Start)
            currentnode = Start
            for n in NODES:
                NODES[n].g = 0
                NODES[n].h = 0
                NODES[n].f = 0
                NODES[n].parent = None

    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(BLACK)
    # Draw a circle
    for i in NODES:
        NODES[i].draw(SCREEN, font1)

    #Draws a circle, showing where you, the user, is on the grid
    pygame.draw.circle(SCREEN, WHITE, (selnode.screenpos[0] + 25, selnode.screenpos[1] + 25), 10)
    pygame.draw.circle(SCREEN, GREEN, (Start.screenpos[0] + 25, Start.screenpos[1] + 25), 10)
    pygame.draw.circle(SCREEN, RED, (End.screenpos[0] + 25, End.screenpos[1] + 25), 10)

    #Draw the lines
    for n in NODES:
        if NODES[n].parent:
            pygame.draw.line(SCREEN, (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240)), (NODES[n].screenpos[0] + 25, NODES[n].screenpos[1] + 25), (NODES[n].parent.screenpos[0] + 25, NODES[n].parent.screenpos[1] + 25), 4)

    if End.parent:
        tmp = End
        while tmp != Start:
            pygame.draw.line(SCREEN, BLACK, (tmp.screenpos[0] + 25, tmp.screenpos[1] + 25), (tmp.parent.screenpos[0] + 25, tmp.parent.screenpos[1] + 25), 4)
            tmp = tmp.parent

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.NODES[n].parent.screenpos[0]
    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()
    

# Be IDLE friendly
pygame.quit()
